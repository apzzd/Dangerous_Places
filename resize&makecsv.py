from GPSPhoto import gpsphoto
import csv, os
from PIL import Image
directory = "photos"
basewidth = 300

for fname in os.listdir(directory):
    img = Image.open(directory + "/" + fname)
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), Image.ANTIALIAS)
    img.save("photos/" + fname)



with open('example.csv', 'w', encoding='UTF8', newline='') as x:
    writer = csv.writer(x)
    writer.writerow(["Latitude", "Longitude", "Tags", "Comment", "Image"])
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        data = gpsphoto.getGPSData(f)
        print(f)
        # image = "<img src='https://raw.githubusercontent.com/apzzd/Dangerous_Places/main/photos/" + filename +"'>"
        writer.writerow([data["Latitude"], data["Longitude"], "", "", ""])
    
