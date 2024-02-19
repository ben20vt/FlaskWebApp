import pandas as pd
import my_LatLong
import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
import Get_Case_Status

INFLUXDB_TOKEN = 'w04oO0vXp-RrUYE7Nj4Wqc9gR0c4KF0IQ9wfsqGQvP5bGt-KWgdYM6RYG4nw6VF_khZNEYaLT1dx1fAUTTMCWQ=='
url = r'https://911events.ongov.net/CADInet/app/_rlvid.jsp?_rap=pc_Cad911Toweb.doLink1Action&_rvip=/events.jsp'

## Read from 911events.ongov.net
tables = pd.read_html(url) # Returns list of all tables on page
table0 = tables[0] # Select table of interest
idx = len(table0)
table = table0.iloc[7:idx-8,0:6]

for index2 in range(len(data_table)):
    Agency = data_table.iloc[index2,0]
    DateandTime = data_table.iloc[index2,1]
    IncidentType = data_table.iloc[index2,2]
    Address = data_table.iloc[index2,3]
    CityJurisdiction = data_table.iloc[index2,4]
    CrossStreets = data_table.iloc[index2,5]
    Status = "Open"
    name = str(Agency + DateandTime + IncidentType + Address + CityJurisdiction + CrossStreets)
    record_ID = hash(name)
    [Lat, Long] = my_LatLong(Address, CrossStreets)
    Status = Get_Case_Status(record_ID)
    if Status == 
            return Status = "Open"
        else:
            return Status = "Closed"
     


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
  

