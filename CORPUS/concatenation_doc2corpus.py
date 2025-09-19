import os
import glob

def concatenate_files():
    # Répertoire courant où le script est exécuté
    current_dir = os.getcwd()
    
    # Nom du fichier de sortie
    output_file = "CORPUS.txt"
    
    # Liste tous les fichiers du répertoire (excluant les dossiers et le fichier de sortie)
    files = [f for f in os.listdir(current_dir) 
             if os.path.isfile(os.path.join(current_dir, f)) 
             and f != output_file 
             and not f.endswith('.py')]  # Exclut aussi les fichiers Python pour éviter d'inclure le script lui-même
    
    if not files:
        print("Aucun fichier trouvé dans le répertoire.")
        return
    
    print(f"Fichiers trouvés : {len(files)}")
    
    try:
        with open(output_file, 'w', encoding='utf-8') as outfile:
            for i, filename in enumerate(sorted(files)):
                print(f"Traitement du fichier {i+1}/{len(files)}: {filename}")
                
                # Ajouter un séparateur avec le nom du fichier
                outfile.write(f"\n{'='*50}\n")
                outfile.write(f"FICHIER: {filename}\n")
                outfile.write(f"{'='*50}\n\n")
                
                try:
                    # Essayer d'abord avec l'encodage UTF-8
                    with open(filename, 'r', encoding='utf-8') as infile:
                        content = infile.read()
                        outfile.write(content)
                        outfile.write('\n\n')
                except UnicodeDecodeError:
                    # Si UTF-8 échoue, essayer avec l'encodage latin-1
                    try:
                        with open(filename, 'r', encoding='latin-1') as infile:
                            content = infile.read()
                            outfile.write(content)
                            outfile.write('\n\n')
                    except Exception as e:
                        outfile.write(f"[ERREUR: Impossible de lire le fichier - {str(e)}]\n\n")
                        print(f"Erreur lors de la lecture de {filename}: {e}")
                
        print(f"\nConcaténation terminée ! Le fichier '{output_file}' a été créé.")
        print(f"Taille du fichier final: {os.path.getsize(output_file)} octets")
        
    except Exception as e:
        print(f"Erreur lors de la création du fichier de sortie: {e}")

if __name__ == "__main__":
    concatenate_files()
