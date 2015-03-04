## Software-based image compression

Module for testing different image compression algorithms. For now we have a JPEG compression code. 

### Requires

For Windows:
```
easy_install Pillow
```

For Linux:
```
sudo pip install Pillow
```

For Mac:
```
brew install libtiff libjpeg webp littlecms
```
```
sudo pip install Pillow
```

### Instructions

To do a quick test, run testimage.py. This takes the input image (testimage.jpg) and compresses it (testimage_compressed.jpg).
To run other tests, import using `from testimage import *` then run `compressionTests('boat.jpg')` for example. 