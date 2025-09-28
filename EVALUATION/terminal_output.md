> 
> # save summary file
> with open(os.path.join(LOG_DIR,'singlefile_chunked_summary.json'),'w',encoding='utf-8') as sf:
>     json.dump(summary,sf,ensure_ascii=False,indent=2)
> 
> print('\nSaved summary to logs/singlefile_chunked_summary.json')
> print(json.dumps(summary, indent=2, ensure_ascii=False))
> PY
🔍 Semantic Analysis - Activation de l'environnement
==================================================
📦 Activation de l'environnement virtuel...
✅ Environnement virtuel activé: venv
📍 Python: /home/.../Documents/SEMANTIC/venv/bin/python
📦 Pip: /home/.../Documents/SEMANTIC/venv/bin/pip

🔍 Vérification des dépendances...
✅ Dépendances déjà installées

🤖 Vérification d'Ollama...
✅ Ollama trouvé: ollama version is 0.11.11
📋 Modèles disponibles:
NAME                ID              SIZE      MODIFIED   
qwen3:30b           e50831eb2d91    18 GB     3 days ago    
gpt-oss:20b         aa4295ac10c3    13 GB     3 days ago    
phi:latest          e2fd6321a5fe    1.6 GB    3 days ago    
mistral:latest      6577803aa9a0    4.4 GB    3 days ago    
✅ 8 modèle(s) installé(s)

🚀 Commandes disponibles:
  streamlit run app.py     - Lancer l'application
  python test_models.py   - Tester les modèles Ollama
  make run                - Lancer avec Makefile
  make test               - Exécuter les tests
  make clean              - Nettoyer le projet

🎉 Environnement prêt ! Vous pouvez maintenant développer.
💡 Tip: Tapez 'deactivate' pour quitter l'environnement virtuel
Models to use: ['phi:latest', 'mistral:latest', 'llama2:latest', 'gemma3:4b-it-qat', 'gemma3:1b', 'deepseek-r1:7b']
File chars: 10333, words: 1675

--- phi:latest
Estimated chunks for model (tokens=4096): 1
❌ Aucune ligne 'A | relation | B' détectée — sortie du modèle peut être en format libre
❌ Aucune ligne 'A | relation | B' détectée — sortie du modèle peut être en format libre
Fallback réalisé mais aucune relation extraite après nettoyage
No pipe found in merged result — running fallback conversion using model

--- mistral:latest
Estimated chunks for model (tokens=4096): 1

--- llama2:latest
Estimated chunks for model (tokens=4096): 1

--- gemma3:4b-it-qat
Estimated chunks for model (tokens=8192): 1
❌ Aucune ligne 'A | relation | B' détectée — sortie du modèle peut être en format libre

--- gemma3:1b
Estimated chunks for model (tokens=1024): 26

--- deepseek-r1:7b
Estimated chunks for model (tokens=8192): 1

Saved summary to logs/singlefile_chunked_summary.json
{
  "phi:latest": {
    "chars": 10333,
    "words": 1675,
    "chosen_tokens": 4096,
    "chunks_estimated": 1,
    "chunks_processed": 1,
    "n_relations": 1,
    "bert_f1": 0.5645960569381714,
    "execution_time_s": 4.048756122589111
  },
  "mistral:latest": {
    "chars": 10333,
    "words": 1675,
    "chosen_tokens": 4096,
    "chunks_estimated": 1,
    "chunks_processed": 1,
    "n_relations": 13,
    "bert_f1": 0.7043166160583496,
    "execution_time_s": 11.6934814453125
  },
  "llama2:latest": {
    "chars": 10333,
    "words": 1675,
    "chosen_tokens": 4096,
    "chunks_estimated": 1,
    "chunks_processed": 1,
    "n_relations": 9,
    "bert_f1": 0.6369527578353882,
    "execution_time_s": 8.772667646408081
  },
  "gemma3:4b-it-qat": {
    "chars": 10333,
    "words": 1675,
    "chosen_tokens": 8192,
    "chunks_estimated": 1,
    "chunks_processed": 1,
    "n_relations": 18,
    "bert_f1": 0.7401612997055054,
    "execution_time_s": 19.860761165618896
  },
  "gemma3:1b": {
    "chars": 10333,
    "words": 1675,
    "chosen_tokens": 1024,
    "chunks_estimated": 26,
    "chunks_processed": 11,
    "n_relations": 92,
    "bert_f1": 0.783343493938446,
    "execution_time_s": 22.182160139083862
  },
  "deepseek-r1:7b": {
    "chars": 10333,
    "words": 1675,
    "chosen_tokens": 8192,
    "chunks_estimated": 1,
    "chunks_processed": 1,
    "n_relations": 12,
    "bert_f1": 0.7029960751533508,
    "execution_time_s": 20.296623706817627
  }
}