import os
import sys
import wget
import shutil
import argparse
import pyeuropeana.apis as apis
import pyeuropeana.utils as utils


def parseArguments():
    parser = argparse.ArgumentParser(description='Europeana Search script')

    parser.add_argument('--europeanaToken',
                        type=str,
                        default='None',
                        help='Europeana Token')
    
    parser.add_argument('--europeanaQuery',
                        type=str,
                        default='None',
                        help='Europeana Query')
    
    parser.add_argument('--outDir',
                        type=str,
                        default='None',
                        help='output Directory')
    
    parser.add_argument('--maxRows',
                        type=int,
                        default=10,
                        help='Max number of results')

    return parser.parse_args()


def setEuropeanaToken(token):
    if ('None' in token):
        sys.exit('Europeana Token is None')
    else:
        os.environ["EUROPEANA_API_KEY"] = token


def checkIsimage(url):
    if (('.jpg' in url) or ('.png' in url)):
        return True
    else:
        return False


def checkOutDir(outDir):
    if (not os.path.exists(outDir)):
        os.mkdir(outDir)


def downloadData(europeanaQuery, outDir, maxRows):
    result = apis.search(
        query = europeanaQuery,
        qf = '(TYPE:IMAGE)',
        reusability = 'open', 
        rows = maxRows,
        colourpalette = '#808080'
    )

    dataframe = utils.search2df(result)

    for index, row in dataframe.iterrows():
        image_url = row.image_url
        if (image_url):
            if (checkIsimage(image_url)):
                basename = os.path.basename(image_url)
                imgFormat = basename.split('.')[1]
                try:
                    wget.download(image_url, out=outDir)

                    srcName = os.path.join(outDir, basename.split('?')[0])
                    europeana_id = (row.europeana_id+'.'+str(imgFormat)).replace('/', '_')
                    newName = outDir+'/'+europeana_id.split('?')[0]
                    os.rename(srcName, newName)
                except:
                    print ("Warning - resource download failed")
    print ('')


if __name__ == "__main__":
    args = parseArguments()

    setEuropeanaToken(args.europeanaToken)

    checkOutDir(args.outDir)

    downloadData(args.europeanaQuery, args.outDir, int(args.maxRows))