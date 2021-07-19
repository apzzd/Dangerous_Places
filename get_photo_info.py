from GPSPhoto import gpsphoto
import csv, os
directory = "photos"


with open('example.csv', 'w', encoding='UTF8', newline='') as x:
    writer = csv.writer(x)
    writer.writerow(["Latitude", "Longitude", "Filename"])
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        data = gpsphoto.getGPSData(f)
        writer.writerow([data["Latitude"], data["Longitude"], filename])
    
