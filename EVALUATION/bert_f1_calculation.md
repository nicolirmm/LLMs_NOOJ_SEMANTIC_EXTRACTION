# Calcul exact du BERT F1 utilisé dans notre projet
# BERT F1 score calculation used in our project

This document explains, step by step and precisely, how the BERT F1 score (`bert_f1`) stored in `logs/singlefile_chunked_summary.json` is computed in our project.

## Checklist
- Locate where the score is computed — `scripts/postprocess_chunked_logs.py` ✓
- Describe preprocessing that builds the candidate string — `src/utils/result_processor.py` ✓
- Explain parameters passed to `bert_score.score` (lang, idf, model) ✓
- Provide the exact formula and algorithm (matching, P, R, F) ✓
- Illustrate how the JSON summary is produced and which code writes the score ✓

---

## 1) Where the score is computed
The computation happens in:

- `scripts/postprocess_chunked_logs.py`

Key excerpt (logic):

- The reference is built from `src/utils/relations_ref/reference_relations_arb.json`:
  - each reference relation becomes a line `sujet | relation | objet ;`
  - `ref_text = '\n'.join(ref_lines)`
- The candidate is the concatenation of relations extracted from the model output:
  - `relations = ResultProcessor.extract_relations(cleaned)` then `cand = '\n'.join(relations)`.
- BERTScore call:

```py
P, R, F1 = score([cand], [ref_text], lang='fr', verbose=False)
summary[model] = {'n_relations': len(relations), 'bert_f1': float(F1[0])}
```

The stored value `bert_f1` is therefore `float(F1[0])` (a single candidate/reference pair).

## 2) How the candidate is built (preprocessing)
All steps live in `src/utils/result_processor.py`:

1. `_remove_thinking_tags` — remove `<think>...</think>` blocks and certain explanatory lines.
2. `_extract_relations_only` — permissive extraction: keep lines with at least two `|` (format `A | rel | B`) and normalize spaces around `|`.
3. `_normalize_format` — ensure a final ` ;` and normalize spacing.
4. `_validate_relations_format` — heuristic mapping of relation labels to canonical labels (e.g. `r_est_un_type_de`), rebuild lines as `entity1 | mapped_relation | entity2 ;`.
5. `extract_relations` — remove final `;` and return a list of normalized lines, each `entity1 | relation | entity2`.

The candidate text (`cand`) passed to BERTScore is these lines joined by newlines.

## 3) `bert_score` parameters and behaviour used
- Call in code: `score([cand], [ref_text], lang='fr', verbose=False)`.
- Implicit default parameters (installed `bert_score` v0.3.13):
  - `model_type` not provided → `bert_score` maps `lang='fr'` to the default `lang2model` entry; for languages not listed the default is `bert-base-multilingual-cased`.
  - `idf=False` (default) → no IDF weighting (uniform weights), except `[CLS]`/`[SEP]` tokens have idf=0.
  - `rescale_with_baseline=False` (default).
  - `device`: CUDA if available else CPU.

Consequence: the score is produced using `bert-base-multilingual-cased` embeddings, without explicit IDF weighting.

## 4) Exact algorithm and formulas (implementation)
The implementation (in `venv/.../site-packages/bert_score/utils.py`) performs:

- Tokenization + BERT encoding → token-level embeddings (normalized by their norm).
- Cosine similarity matrix `sim[i, j] = cosine(hyp_token_i, ref_token_j)`.
- Remove special tokens ([CLS], [SEP]) before matching.
- Word-level scores:
  - for each candidate token i: `word_precision[i] = max_j sim[i, j]` (best matching reference token)
  - for each reference token j: `word_recall[j] = max_i sim[i, j]`
- Weighting (with `idf=False` the idf vectors are uniform after normalization):
  - P = sum_i word_precision[i] * w_i, where w_i = hyp_idf[i] / sum(hyp_idf) (≈ 1/|hyp_tokens|)
  - R = sum_j word_recall[j] * v_j, where v_j = ref_idf[j] / sum(ref_idf)
- F1 (per pair): `F = 2 * P * R / (P + R)` (NaN → 0 if P+R == 0)

These operations are implemented inside `bert_cos_score_idf` → `greedy_cos_idf`.

## 5) Edge cases and observed behaviours
- If the candidate (`cand`) is empty, `postprocess_chunked_logs.py` writes `bert_f1 = 0.0`.
- `[CLS]` and `[SEP]` tokens have idf 0 and do not contribute.
- No IDF ⇒ each token has equal weight (after normalization).
- The chosen pretrained model (multilingual vs monolingual) significantly affects the score.

## 6) Practical illustration (how the JSON logs are produced)
Simplified flow for one run:

1. A model run produced `logs/*.chunked.json` files with the raw outputs.
2. `postprocess_chunked_logs.py` reads each file, cleans using `ResultProcessor.clean_result(...)`, extracts relations and then:
   - writes `logs/<name>.A.txt` and `logs/<name>.B.txt` (copies of relations)
   - computes BERTScore with `score([cand], [ref_text], lang='fr')`
   - updates `summary[model] = {'n_relations': len(relations), 'bert_f1': float(F1[0])}`
3. Finally the global summary is written:

```py
with open(os.path.join(LOG_DIR, 'singlefile_chunked_summary.json'), 'w', encoding='utf-8') as sf:
    json.dump(summary, sf, ensure_ascii=False, indent=2)
```

The resulting JSON object matches the example you provided: one entry per model with `n_relations` and `bert_f1`.

## 7) Quick reproduction
To reproduce the postprocessing and obtain the same `singlefile_chunked_summary.json`:

```bash
python scripts/postprocess_chunked_logs.py
```

(this script reads `logs/*.chunked.json` and writes `logs/postprocess_summary.json` and/or `logs/singlefile_chunked_summary.json` depending on the flow in your repo)

## 8) Notes and improvement suggestions
- If we want to control the BERT model used (e.g. `roberta-large`), change the call:

```py
P, R, F1 = score([cand], [ref_text], model_type='roberta-large', lang=None)
```

- To enable real IDF weighting, call `score(..., idf=True)`.
- For deeper debugging, we can add a script that prints the token×token similarity matrix and token-level P/R/F for a candidate/reference pair.

---

Files consulted for this document :
- `scripts/postprocess_chunked_logs.py`
- `src/utils/result_processor.py`
- `venv/lib64/python3.12/site-packages/bert_score/score.py`
- `venv/lib64/python3.12/site-packages/bert_score/utils.py`

If you want, we can:
- generate the debug script mentioned (matrix + tokens + P/R/F detailed), and run it for one of the models listed in your summary; or
- add a short note to the repository README linking to this Markdown.


Files consulted for this document / Fichiers consultés pour ce document :
- `scripts/postprocess_chunked_logs.py`
- `src/utils/result_processor.py`
- `venv/lib64/python3.12/site-packages/bert_score/score.py`
- `venv/lib64/python3.12/site-packages/bert_score/utils.py`

If you want, we can:
- generate the debug script mentioned (matrix + tokens + P/R/F detailed), and run it for one of the models listed in your summary; or
- add a short note to the repository README linking to this Markdown.
