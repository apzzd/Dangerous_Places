from PIL import Image
import os
basewidth = 300

for fname in os.listdir(directory):
    img = Image.open(directory + "/" + fname)
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), Image.ANTIALIAS)
    img.save("photos/" + fname)