from PIL import Image, ImageMath
from random import randint

im = Image.open("thermalpng.png")
pixdata = im.load()
plouse = 0
coco = []
mama = []

r = randint(0, 255)
g = randint(0, 255)
b = randint(0, 255)

lmao = (r, g, b, 255)

for y in xrange(im.size[1]):
   for x in xrange(im.size[0]):
       if (pixdata[x, y][0]+pixdata[x, y][1]+pixdata[x, y][2]>600):
           coco.append([x, y])
           pixdata[x, y] = lmao

for [x, y] in coco:
	if ((pixdata[x+1, y] != lmao) or (pixdata[x-1, y] != lmao) or (pixdata[x, y+1] != lmao) or (pixdata[x, y-1] != lmao)):
		mama.append(lmao)
		pixdata[x, y] = (lmao)
		plouse = plouse + 1
	else:
		r = randint(0, 255)
		g = randint(0, 255)
		b = randint(0, 255)

		lmao = (r, g, b, 255)



print str(plouse)



im.show(im)