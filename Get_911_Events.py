import pandas as pd
import my_LatLong
import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
import QueryDB
from numpy import nan
import hashlib
import CloseAllCases
import TrimIngestData

INFLUXDB_TOKEN = 'w04oO0vXp-RrUYE7Nj4Wqc9gR0c4KF0IQ9wfsqGQvP5bGt-KWgdYM6RYG4nw6VF_khZNEYaLT1dx1fAUTTMCWQ=='
url = r'https://911events.ongov.net/CADInet/app/_rlvid.jsp?_rap=pc_Cad911Toweb.doLink1Action&_rvip=/events.jsp'

## Read from 911events.ongov.net
tables = pd.read_html(url) # Returns list of all tables on page
table = tables[6] # Select table of interest
length = len(table)
table = table.drop([length - 1])

## Initialize Database
token = INFLUXDB_TOKEN
org = "User-Space"
url2 = "http://10.50.1.101:8086"

write_client = influxdb_client.InfluxDBClient(url=url2, token=token, org=org)
bucket="OnondagaCountyiCAD"
write_api = write_client.write_api(write_options=SYNCHRONOUS)

sha256_hash = hashlib.new("SHA256")
Active_Records = []



## Process Table to DB
for index2 in range(len(table)):
    Agency = table.iloc[index2,0]
    if str(Agency) == 'nan':
        Agency = "Unavailable"
    else:
        Agency = str(table.iloc[index2,0])

    DateandTime = table.iloc[index2,1]
    if str(DateandTime) == 'nan':
        DateandTime = "Unavailable"
    else:
        DateandTime = str(table.iloc[index2,1])

    # #IncidentType = table.iloc[index2,2]
    # if IncidentType == "Unknown":
    #     IncidentType = "Unknown"
    # else:
    #     IncidentType = str(IncidentType_DB.iloc[index2,2])


    IncidentType = table.iloc[index2,2]
    if str(IncidentType) == 'nan':
        IncidentType = "Unknown"
    else:
        IncidentType = str(table.iloc[index2,2])
        
    Address = table.iloc[index2,3]
    if str(Address) == 'nan':
        Address = ""
    else:
        Address = str(table.iloc[index2,3])

    CityJurisdiction = table.iloc[index2,4]
    if str(CityJurisdiction) == 'nan':
        CityJurisdiction = "Unavailable"
    else:
        CityJurisdiction = str(table.iloc[index2,4])

    CrossStreets = table.iloc[index2,5]
    if str(CrossStreets) == 'nan':
        CrossStreets = ""
    else:
        CrossStreets = str(table.iloc[index2,5])

    Status = "Open"
    name = str(Agency + DateandTime + IncidentType + Address + CityJurisdiction + CrossStreets)
    sha256_hash.update(name.encode())
    
    record_ID = sha256_hash.hexdigest()
    
    [Lat, Long] = my_LatLong.my_LatLong(Address, CrossStreets)

    Exist = QueryDB.QueryDB(record_ID)
    if Exist == 1:
       Status = "Open" 
    else:
        Status = "Open"
        point = (
            Point("911Events")
            .field("Status", Status)
            .tag("record_ID", record_ID)
            .tag("Date/Time", DateandTime)
            .tag("Agency", Agency)
            .tag("Incident Type", IncidentType)
            .tag("City Jurisdiction", CityJurisdiction)
            .tag("Latitude", Lat)
            .tag("Longitude", Long)
        )
        write_api.write(bucket=bucket, org="User-Space", record=point)
    
        Active_Records.append(record_ID)
    #CloseAllCases.CloseAllCases(Active_Records)
  

