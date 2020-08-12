

from wand.image import Image
with Image(filename='004.png') as img:
    img.type = 'grayscale'
    img.save(filename='grayscale000.jpg')

import PIL.Image
rgba_image = PIL.Image.open('004.png')
rgb_image = rgba_image.convert('RGB')
rgb_image.save("005.jpg", "JPEG", quality=100)

from PIL import Image
im1 = Image.open("005.jpg")
'''im2 = Image.open("grayscale000.jpg")
im3 = Image.open("000.png")'''
im_list = [im1]
''',im2,im3]'''

pdf1_filename = "bbd1.pdf"

#im1.save(pdf1_filename, "PDF" ,resolution=100.0, save_all=True, append_images=im_list)    
im1.save(pdf1_filename, "PDF" ,resolution=100.0, save_all=True)      


