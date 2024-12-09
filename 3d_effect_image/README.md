# 3d_photo
The script allows two separate processes to be executed, one to search for data via the Europeana API and the other to apply 3D effects on images, with configuration parameters passed via the command line. Its flexibility allows it to handle different operations depending on the process required, supporting execution on both Linux and WSL systems.

## Gestione degli argomenti della riga di comando
- The script uses argparse to collect command-line input, such as the type of process to be executed (--process), the output directory (--outDir), and other process-specific configurations (e.g. Europeana search token, query and maximum number of results).

## Processo Europeana
- If the --process parameter contains the string ‘europeana’, the script starts a search via the Europeana API, using the parameters --europeanaToken, --europeanaQuery, and --maxRows. The result is saved in the specified output directory.

## Processo 3D Effect Image
- If the --process parameter contains the string ‘effect_3d’, the script executes a 3D effect on the input image using the 3d_photo.py module, specifying the type of 3D effect via the --effect_3d parameter (options: ‘dolly-zoom-in’, ‘zoom-in’, ‘circle’, ‘swing’).

## Supporto per esecuzione tramite WSL
- There is also a --wsl parameter indicating whether the script is to be executed via Windows Subsystem for Linux (WSL).

## Gestione degli errori
- If the --process parameter does not match one of the two valid values (‘european’ or ‘effect_3d’), the script terminates with an error.