import os

from PIL import Image

from util.refactor import refactor_img


list_img = os.listdir(path="img/input_img")

for img in list_img:
    if not img.endswith('gif'):
        image = Image.open(f'img/input_img/{img}')
        image.save(f'img/input_img/{img.split(".")[0]+".gif" }', 'gif')
        os.remove(f'img/input_img/{img}')


for img in os.listdir(path="img/input_img"):
    refactor_img(f'img/input_img/{img}')
