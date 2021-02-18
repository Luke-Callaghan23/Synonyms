
map = [
    {
        'new_rgb' : (19, 69, 99, 255),
        'old_rgb' : (37, 37, 37, 255)
    },
    {
        'new_rgb' : (19, 69, 99, 255),
        'old_rgb' : (38, 38, 38)
    },
    {
        'new_rgb' : (255, 255, 255, 000),
        'old_rgb' : (255, 255, 255, 000)
    },
    {
        'new_rgb' : (255, 255, 255, 000),
        'old_rgb' : (252, 252, 252, 000)
    },
    
]

from sys import argv
from PIL import Image
picture = Image.open(argv[1])

# Get the size of the image
width, height = picture.size

# Process every pixel
for x in range(width):
    for y in range(height):
        current_color = picture.getpixel( (x,y) )
        # print(current_color)
        for mapping in map:
            if (
                current_color[0] == mapping['old_rgb'][0] and 
                current_color[1] == mapping['old_rgb'][1] and 
                current_color[2] == mapping['old_rgb'][2]
            ):
                picture.putpixel( (x,y), mapping['new_rgb'])
            elif (
                current_color[0] > 250 and
                current_color[1] > 250 and
                current_color[2] > 250
            ):
                picture.putpixel( (x,y), (255,255,255,000))
                


picture.save(f'{argv[1]}2.png');