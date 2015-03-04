import os
from PIL import Image

def generateOutfile(infile):
	base,e = os.path.splitext(infile)
	return base+"_compressed.jpg"

def compress(infile,outfile,algorithm='JPEG',quality=10,BW=False):
    try:
        if BW: # black and white
            compImg = Image.open(infile).convert("L")
        else:  # full colour
            compImg = Image.open(infile)
        compImg.save(outfile,algorithm,quality=quality)
        print "compressed %s to %s" % (infile,outfile)

    except IOError:
        print "cannot convert", infile

def compRatio(origFile,compFile):
    origSize = os.path.getsize(origFile)
    compSize = os.path.getsize(compFile)
    return float(compSize)/float(origSize)

## Main
if __name__ == "__main__":
    infile = 'testimage.jpg'
    outfile = generateOutfile(infile)
    compress(infile,outfile)
    print "Compression ratio is %f" % compRatio(infile,outfile)
