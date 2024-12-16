import os
import sys
import argparse


def parseArguments():
    parser = argparse.ArgumentParser(description='Main')

    parser.add_argument('--process',
                        type=str,
                        default='None',
                        help='Specify Process [europeana or effect3d]')

    parser.add_argument('--outDir',
                        type=str,
                        default='None',
                        help='Output Directory')

    """
    European Search Params
    """
    parser.add_argument('--europeanaToken',
                        type=str,
                        default='None',
                        help='Europeana Token')
    
    parser.add_argument('--europeanaQuery',
                        type=str,
                        default='None',
                        help='Europeana Query')
    
    parser.add_argument('--maxRows',
                        type=str,
                        default='10',
                        help='Max number of results')

    """
    3d effect Image Param
    """
    parser.add_argument('--input',
                        type=str,
                        default='None',
                        help='Input image - Only for effect3d process')
    
    parser.add_argument('--effect3d',
                        type=str,
                        default='dolly-zoom-in',
                        help='Specify 3D effect ["dolly-zoom-in", "zoom-in", "circle", "swing"] - Only for effect3d process')
    
    parser.add_argument('--wsl',
                        type=str,
                        default='True',
                        help='Specifies whether the script is executed via WSL or not. [default=True]')

    return parser.parse_args()


if __name__ == "__main__":
    args = parseArguments()

    if ('europeana' in args.process.lower()):
        output = os.path.join(args.outDir, 'europeana')
        os.system('python /3d-photo-inpainting/europeana_search.py --europeanaToken '+str(args.europeanaToken)+' --europeanaQuery '+str(args.europeanaQuery)+' --outDir '+str(output)+' --maxRows '+str(args.maxRows))
    elif ('effect3d' in args.process.lower()):
        os.system('python /3d-photo-inpainting/3dEffect.py --input '+str(args.input)+' --output '+str(args.outDir)+' --effect3d '+str(args.effect3d)+' --wsl '+str(args.wsl))
    else:
        sys.exit('Eroor - process must be "europeana" or "effect3d"')
