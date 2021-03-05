from PIL import Image
import io
import pathlib

im = Image.open('test.png')

im2 = Image.open(pathlib.Path('test.png'))

f = open('test.png', 'rb')
im3 = Image.open(f)

with open('test.png', 'rb') as f:
    im4 = Image.open(io.BytesIO(f.read()))

