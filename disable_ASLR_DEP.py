import argparse
import pefile
import mmap

def disable_aslr_and_dep(file_path, outfile_path, disable_aslr, disable_dep):
    try:
        # Charger le fichier PE
        with open(file_path, 'r+b') as file:
            pe_data = mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ)
            pe = pefile.PE(data=pe_data)

            # Désactiver ASLR (Address Space Layout Randomization)
            if disable_aslr:
                pe.OPTIONAL_HEADER.DllCharacteristics &= ~pefile.DLL_CHARACTERISTICS['IMAGE_DLLCHARACTERISTICS_DYNAMIC_BASE']
            
            # Désactiver DEP (Data Execution Prevention)
            if disable_dep:
                pe.OPTIONAL_HEADER.DllCharacteristics &= ~pefile.DLL_CHARACTERISTICS['IMAGE_DLLCHARACTERISTICS_NX_COMPAT']
            
            # Enregistrer les modifications dans le fichier
            pe.write(outfile_path)

            print("ASLR et DEP désactivés avec succès.")
    except Exception as e:
        print("Une erreur s'est produite:", e)

# Fonction principale
def main():
    # Analyse des arguments de la ligne de commande
    parser = argparse.ArgumentParser(description="Désactiver l'ASLR et/ou le DEP dans un fichier PE.")
    parser.add_argument("-f", "--file", help="Chemin vers le fichier PE", required=True)
    parser.add_argument("-o", "--outfile", help="Chemin vers le fichier de sortie (fichier créé)", required=True)
    parser.add_argument("-a", "--disable_aslr", help="Désactiver l'ASLR", action="store_true")
    parser.add_argument("-d", "--disable_dep", help="Désactiver le DEP", action="store_true")
    args = parser.parse_args()

    # Appel de la fonction pour désactiver ASLR et/ou DEP
    disable_aslr_and_dep(args.file, args.outfile, args.disable_aslr, args.disable_dep)

# Exécution du script
if __name__ == "__main__":
    main()
