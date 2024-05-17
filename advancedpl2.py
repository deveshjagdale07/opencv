from PIL import Image
import matplotlib.pyplot as plt
img1=Image.open("rose.jpg")
img2=Image.open("orange.jpg")
img1.paste(img2,(100,200))
img1.show()

histogram=img1.histogram()
plt.hist(histogram,bins=len(histogram))
plt.xlabel("histogram")
plt.show()

transposed_img=img1.transpose(Image.FLIP_LEFT_RIGHT)
transposed_img.show()

red,green,blue=img1.split()
zero=red.point(lambda _: 0)
red=Image.merge("RGB",(red,zero,zero))
green=Image.merge("RGB",(zero,green,zero))
blue=Image.merge("RGB",(zero,zero,blue))
red.show()
green.show()
blue.show()

img1.save(new_img.bmp)

MAX_SIZE=(100,200)
img2.thumbnail(MAX_SIZE)
img2.save("thumbnail")
