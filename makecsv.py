from GPSPhoto import gpsphoto
import csv, os
directory = "newPhotos"



with open('data2.csv', 'w', encoding='UTF8', newline='') as x:
    writer = csv.writer(x)
    writer.writerow(["Latitude", "Longitude", "Tags", "Comment", "Image"])
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        data = gpsphoto.getGPSData("/newPhotos/IMG_1179.jpeg")
        print(f)
        image = "<img src='https://raw.githubusercontent.com/apzzd/Dangerous_Places/main/otherPhotos/" + filename +"'>"
        writer.writerow([data["Latitude"], data["Longitude"], "[tag]", "[comment]", image])
    
