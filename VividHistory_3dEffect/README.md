# VividHistory_3dEffect
The script allows two separate processes to be executed, one to search for data via the Europeana API and the other to apply 3D effects on images, with configuration parameters passed via the command line. Its flexibility allows it to handle different operations depending on the process required, supporting execution on both Linux and WSL systems.

## Handling of command line arguments
- The script uses argparse to collect command-line input, such as the type of process to be executed (--process), the output directory (--outDir), and other process-specific configurations (e.g. Europeana search token, query and maximum number of results).

## Europeana' process
- If the --process parameter contains the string ‘europeana’, the script starts a search via the Europeana API, using the parameters --europeanaToken, --europeanaQuery, and --maxRows. The result is saved in the specified output directory.

## 3D effect' process
- If the --process parameter contains the string ‘effect_3d’, the script executes a 3D effect on the input image using the 3dEffect.py module, specifying the type of 3D effect via the --effect_3d parameter (options: ‘dolly-zoom-in’, ‘zoom-in’, ‘circle’, ‘swing’).

## Support for execution via WSL
- There is also a --wsl parameter indicating whether the script is to be executed via Windows Subsystem for Linux (WSL).

## Error management
- If the --process parameter does not match one of the two valid values (‘european’ or ‘effect_3d’), the script terminates with an error.

# Installation
In the folder provided is the `Dockerfile`, which contains all the libraries required for the application to function correctly. Alternatively, you can download the pre-compiled image directly from Docker Hub by running the following command:

`docker pull 3domfbk/vividhistory_3deffect:<tag>`

## Example
Below is an example:

`docker run --rm -it --gpus all --privileged -v <_HOST_PATH_>:/data 3domfbk/vividhistory_3deffect:<tag> --process effect3d --outDit /data --input /data/<_IMG_NAME>.jpg`

<img src="assets/img_in.jpeg" alt="input image" width="400" />

<img src="assets/img_out.gif" alt="output video" width="400" />