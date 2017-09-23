from __future__ import print_function
import os
import pandas as pd
import numpy as np
import urllib2
import sys
import json

#Sys Arg
if len(sys.argv) != 4:
    print("You did not enter the appropriate number of arguments. Please try again")
    sys.exit()

mta_key = sys.argv[1]
bus_line = sys.argv[2]
bus_line_csv = sys.argv[3]

#Reading the Data 

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + mta_key + "&VehicleMonitoringDetailLevel=calls&LineRef=" + bus_line
response = urllib2.urlopen(url)
data = response.read()
data = json.loads(data)

#Drilling down to Each Independent Bus

indbus = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

#Creating the Data List & Populating the Dataframe

datalist = []

for i in indbus:
    dict = {}
    dict['Longitude'] = str(i['MonitoredVehicleJourney']['VehicleLocation']['Longitude'])
    dict['Latitude'] = str(i['MonitoredVehicleJourney']['VehicleLocation']['Latitude'])
    dict['Stop'] = str(i['MonitoredVehicleJourney']['MonitoredCall']['StopPointName'])
    dict['Status'] = str(i['MonitoredVehicleJourney']['MonitoredCall']['Extensions']['Distances']['PresentableDistance'])
    datalist.append(dict)

df = pd.DataFrame(datalist)

#Writing the Dataframe to CSV File

df.to_csv(str(bus_line_csv))







