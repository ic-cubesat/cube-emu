import os
from PIL import Image

def generateOutfile(infile):
	base,e = os.path.splitext(infile)
	return base+"_compressed.jpg"

def compress(infile,outfile,quality=10):
	try:
		compImg = Image.open(infile).convert("L")
		compImg.save(outfile,"JPEG",quality=quality)
		print "compressed %s to %s" % (infile,outfile)
	except IOError:
		print "cannot convert", infile

## Main
infile = 'testimage.jpg'
outfile = generateOutfile(infile)
compress(infile,outfile)

