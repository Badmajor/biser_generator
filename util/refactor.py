from statistics import mean

from PIL import Image, ImageDraw


def resize_img(path, height_new=0):
    global new_image, width_new
    image = Image.open(path)
    width, height = image.size  # tuple
    if height_new > 0:
        width_new = height_new * width//height
        image_new = image.resize((width_new, height_new), Image.ANTIALIAS)


def refactor_img(path):
    img = Image.open(path)
    width, height = img.size
    idraw = ImageDraw.Draw(img)
    for j in range(width // 8 + 1):
        for i in range(height // 8 + 1):
            coord = (j * 8, i * 8, j * 8 + 8, i * 8 + 8)
            crop = img.crop(coord)
            color = int(mean(list(crop.getdata())))
            idraw.rectangle(coord, fill=15)
            idraw.ellipse(coord, fill=color)
    img.show()

"""cropped = image.crop((0, 0, 8, 8))
    
    idraw = ImageDraw.Draw(image)
    #idraw.rectangle((0, 0, 8, 8), fill=64)
    #idraw.ellipse((26, 0, 34, 8), fill=40)
    list_pix = list(image.getdata())
    print(list_pix)
    image.show()"""
