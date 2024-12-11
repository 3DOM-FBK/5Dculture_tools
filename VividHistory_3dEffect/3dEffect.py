import os
import shutil
import sys
import argparse


def argumentsParse():
    parser = argparse.ArgumentParser(description='3d photo effect')
    parser.add_argument('--input', type=str, default=None, help='Input image, Only .jpg image')
    parser.add_argument('--output', type=str, default=None, help='Output folder')
    parser.add_argument('--effect_3d', type=str, default="dolly-zoom-in", help='Specify 3D effect ["dolly-zoom-in", "zoom-in", "circle", "swing"]')
    parser.add_argument('--wsl', type=str, default="True", help='Specifies whether the script is executed via WSL or not. [default=True]')

    args = parser.parse_args()
    return args


def resetImageFolder():
    files = os.listdir(os.path.join("/3d-photo-inpainting", "image"))
    for f in files:
        os.remove(os.path.join("/3d-photo-inpainting", "image", f))


def resetVideoFolder():
    files = os.listdir(os.path.join("/3d-photo-inpainting", "video"))
    for f in files:
        os.remove(os.path.join("/3d-photo-inpainting", "video", f))


def resetDepthFolder():
    files = os.listdir(os.path.join("/3d-photo-inpainting", "depth"))
    for f in files:
        os.remove(os.path.join("/3d-photo-inpainting", "depth", f))


def checkInputImage(img):
    if (".jpg" not in img):
        print ("Error - Only .jpg file are allowed")
        sys.exit()

if __name__ == "__main__":
    args = argumentsParse()

    resetImageFolder()
    resetVideoFolder()
    resetDepthFolder()

    checkInputImage(args.input)

    try:
        shutil.copy(args.input, os.path.join("/3d-photo-inpainting", "image"))
    except:
        print ("Error - Copy input image into image folder")
        sys.exit()
    
    effect_3d = {
        "dolly-zoom-in": "argument_dolly_zoom_in.yml",
        "zoom-in": "argument_zoom_in.yml",
        "circle": "argument_circle.yml",
        "swing": "argument_swing.yml"
    }
    
    if (args.wsl.lower() == "true"):
        os.system("MKL_THREADING_LAYER=GNU xvfb-run python main.py --config " + effect_3d[args.effect_3d])
    else:
        os.system("xvfb-run python main.py --config " + effect_3d[args.effect_3d])
    
    try:
        files = os.listdir(os.path.join("/3d-photo-inpainting", "video"))
        for f in files:
            src = os.path.join("/3d-photo-inpainting", "video", f)
            dest = os.path.join(args.output, f)
            shutil.copy(src, dest)

        # shutil.copytree(os.path.join("/3d-photo-inpainting", "video"), args.output)
    except:
        print ("Error - Copy video output files into output folder")
        sys.exit()
