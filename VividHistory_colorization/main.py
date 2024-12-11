import os
import sys
import argparse


def parseArguments():
    parser = argparse.ArgumentParser(description='Main')

    parser.add_argument('--process',
                        type=str,
                        default='None',
                        help='Specify Process [europeana or colorize]')

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
    Colorize Image Param
    """
    parser.add_argument('--input',
                        type=str,
                        default='None',
                        help='Input image [Only for Colorize process]')

    return parser.parse_args()


if __name__ == "__main__":
    args = parseArguments()

    if ('europeana' in args.process.lower()):
        output = os.path.join(args.outDir, 'europeana')
        os.system('python /usr/src/scripts/europeana_search.py --europeanaToken '+str(args.europeanaToken)+' --europeanaQuery '+str(args.europeanaQuery)+' --outDir '+str(output)+' --maxRows '+str(args.maxRows))
    elif ('colorize' in args.process.lower()):
        os.system('python /usr/src/scripts/img_colorization.py --input '+str(args.input)+' --process_order DeOldify --output '+str(args.outDir))
    else:
        sys.exit('Eroor - process must be "europeana" or "colorize"')
