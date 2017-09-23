#Imports
from __future__ import print_function
import pandas as pd
import os
import numpy as np
import urllib2
import sys
import json

#Sys Arg
if len(sys.argv) != 3:
    print("You did not enter the appropriate number of arguments. Please try again")
    sys.exit()

mta_key = sys.argv[1]
bus_line = sys.argv[2]

#Reading the Data   

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + mta_key + "&VehicleMonitoringDetailLevel=calls&LineRef=" + bus_line
response = urllib2.urlopen(url)
data = response.read()
data = json.loads(data)


#Drilling down to each independent bus
indbus = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']


##########################
#Output

#Name of bus line
print("Bus Line: "+ bus_line)


#Number of active busses
num_bus = str(len(indbus))
print("Number of Active Busses: " + num_bus)

#Location of each independent bus
busno = 0
for i in indbus:
    longitude = str(i['MonitoredVehicleJourney']['VehicleLocation']['Longitude'])
    latitude = str(i['MonitoredVehicleJourney']['VehicleLocation']['Latitude'])
    print("Bus " + str(busno) + " is at latitude " + latitude + " and longitude " + longitude)
    busno += 1