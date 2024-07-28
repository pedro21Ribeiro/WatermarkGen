from working import addWatermark
from PIL import Image
from os import walk
from os.path import splitext

def func(PATH, waterMark, output):
    files = []
    for(dirpath, dirnames, filenames) in walk(PATH):
        files.extend(filenames)
        break

    watermark = Image.open(waterMark)


    for file in files:
        base = Image.open(f"{PATH}/{file}")
        w, h = base.size
        if(w<h):
            Min = w
        else:
            Min = h
        watermark = watermark.resize((int(Min/5), int(Min/5)))
        done = addWatermark(base, watermark)
        done.save(f"{output}/{splitext(file)[0]}.png")
