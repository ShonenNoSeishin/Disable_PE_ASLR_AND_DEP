<a href="https://www.buymeacoffee.com/thibaut_watrisse" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>

# Disable_PE_ASLR_AND_DEP
Python script to disable ASLR and/or DEP on PE file 

## How to use it

````bash
# -a is to disable ASLR
# -d is to disable DEP
python disable_ASLR_DEP.py -f <path_to_exe> -a -d -o <path_to_outfile>
`````

You can also get help with -h but it is in French. 

````bash
python disable_ASLR_DEP.py -h
usage: disable_ASLR_DEP.py [-h] -f FILE -o OUTFILE [-a] [-d]

Désactiver l'ASLR et/ou le DEP dans un fichier PE.

options:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  Chemin vers le fichier PE
  -o OUTFILE, --outfile OUTFILE
                        Chemin vers le fichier de sortie (fichier créé)
  -a, --disable_aslr    Désactiver l'ASLR
  -d, --disable_dep     Désactiver le DEP
````

## Credits

A huge thanks to <a href="https://github.com/MastMind" target="_blank">MastMind</a>, this script is inspired of a part of his PE-Infector project.

## Enjoy
