from GPSPhoto import gpsphoto
import csv, os
directory = "photosForData"



with open('example.csv', 'w', encoding='UTF8', newline='') as x:
    writer = csv.writer(x)
    writer.writerow(["Latitude", "Longitude", "Tags", "Comment", "Image"])
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        data = gpsphoto.getGPSData(f)
        print(f)
        image = "<img src='https://raw.githubusercontent.com/apzzd/Dangerous_Places/main/photos/" + filename +"'>"
        writer.writerow([data["Latitude"], data["Longitude"], "[tag]", "[comment]", image])
    
