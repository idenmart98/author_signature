
import os
import glob
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import click
import os


@click.command()
@click.option('--way', default='output-images', help='Number of greetings.')
def signature(way):
    if way == 'output-images' and not os.path.exists(way):
        os.mkdir(way) 
    font = ImageFont.truetype('fonts/font1.ttf', size=25)
    for filename in glob.glob('source-images/*.jpg'):
        im = Image.open(filename)
        draw_text = ImageDraw.Draw(im)
        name = os.path.basename(filename)
        index = name.index('.')
        size = draw_text.textsize('©'+' '+name[:index], font=font)
        draw_text.text(
            (im.width-(size[0]+7), im.height-(size[1]+7)),
            '©'+' '+name[:index],
            font=font,
            fill=('#808080')
            )
        filepath = way+'/'+name 
        im.save(filepath)

if __name__ == '__main__':
    signature()