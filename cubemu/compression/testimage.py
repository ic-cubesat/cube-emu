import os
from PIL import Image
def compressLoop(infile , times):
	n=2
	base, e = os.path.splitext(infile)
	try:
			f,e = os.path.splitext(infile)
			f = (base + str(n))
			outfile = f + ".jpg"
			compImg = Image.open(infile).convert("L")
			compImg.save(outfile, "JPEG", quality = 10)
			infile = outfile 
	except IOError:
		print "cannot convert", infile

infile = raw_input ("Filename to compress:")
times = int(input ("Times to process: "))
compressLoop(infile,times)


