import pandas as pd
import geopy.geocoders
from geopy.geocoders import Nominatim
import numpy as np
import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS


INFLUXDB_TOKEN = 'w04oO0vXp-RrUYE7Nj4Wqc9gR0c4KF0IQ9wfsqGQvP5bGt-KWgdYM6RYG4nw6VF_khZNEYaLT1dx1fAUTTMCWQ=='
url = r'https://911events.ongov.net/CADInet/app/_rlvid.jsp?_rap=pc_Cad911Toweb.doLink1Action&_rvip=/events.jsp'

## Read from 911events.ongov.net
tables = pd.read_html(url) # Returns list of all tables on page
table0 = tables[0] # Select table of interest
idx = len(table0)
table = table0.iloc[7:idx-8,0:6]

## Change Crossstreets to Addresses
#geolocator = Nominatim(user_agent="my-application") # format_string="%s, Onondaga County, NY"

# num_records = len(table)

# Lat = np.zeros(num_records)
# Long = np.zeros(num_records)
 
# table.insert(6, "Lat", Lat)
# table.insert(7, "Long", Long)

# def get_coordinates_from_cross_streets(city, crossstreets):
#         geolocator = Nominatim(user_agent="cross-streets-locator")
#         location = geolocator.geocode(f"{crossstreets},{city}")
#         if location:
#             return location.latitude, location.longitude
#         else:
#             return None, None

# city = "Syracuse"

# for i in table.iloc[:,5]:
#     n = 0
#     crossstreets = i
#     latitude, longitude = get_coordinates_from_cross_streets(city, crossstreets)
#     table.iloc[n,6] = latitude
#     table.iloc[n,7] = longitude
#     n = n+1


#Check if case is active
def get_status_
(Agency, Date, IncidentType, Address, Jurisdiction, CrossStreets):
        if location:
            return location.latitude, location.longitude
        else:
            return None, None
## Prepare for Writing to DB
token = INFLUXDB_TOKEN
org = "User-Space"
url2 = "http://10.50.1.101:8086"

write_client = influxdb_client.InfluxDBClient(url=url2, token=token, org=org)
bucket="Data2"
write_api = write_client.write_api(write_options=SYNCHRONOUS)

# Preparing Dataframe: 
table.set_index("Date/Time")
for index in range(len(table)):
  point = (
    Point("911Events")
    .field("Status", status)
    .tag("Agency", table.iloc[index,0])
    .tag("Incident Type", table.iloc[index,2])
    .tag("Address", table.iloc[index,3])
    .tag("City Jurisdiction", table.iloc[index,4])
    .tag("Cross Streets", table.iloc[index,5])
  )
  write_api.write(bucket=bucket, org="User-Space", record=point)
  

