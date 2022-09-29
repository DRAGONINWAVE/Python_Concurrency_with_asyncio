from PIL import Image
import numpy as np
im = Image.open(r'D:\\piles\SPEI-1\\SPEI-1\\SPEI313.tif')
im.show()
imarray = np.array(im)
print(imarray.shape)
print(im.size)
print(imarray)
