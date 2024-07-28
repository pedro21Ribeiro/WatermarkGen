from PIL import Image

#def watermark_with_transparency(input_image_path,
#                                output_image_path,
#                                watermark_image_path,
#                                position):
#    base_image = Image.open(input_image_path)
#    watermark = Image.open(watermark_image_path)
#    width, height = base_image.size
#
#    transparent = Image.new('RGBA', (width, height), (0,0,0,0))
#    transparent.paste(base_image, (0,0))
#    transparent.paste(watermark, position, mask=watermark)
#    transparent.show()
#    transparent.save(output_image_path)
#
#
#if __name__ == '__main__':
#    img = './materials/Image.jpg'
#    watermark_with_transparency(img, './materials/ImageDone.jpg',
#                                './materials/waterMark.png', position=(0,0))

def addWatermark(baseImg, watermark):
    width, heigth = baseImg.size

    
    transparent = Image.new("RGBA", (width, heigth), (0, 0, 0, 0))
    transparent.paste(baseImg, (0, 0))
    transparent.paste(watermark, (width - watermark.size[0], heigth - watermark.size[1]), mask=watermark)
    return transparent