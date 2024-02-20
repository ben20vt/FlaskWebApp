import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

token = 'w04oO0vXp-RrUYE7Nj4Wqc9gR0c4KF0IQ9wfsqGQvP5bGt-KWgdYM6RYG4nw6VF_khZNEYaLT1dx1fAUTTMCWQ=='
org = "User-Space"
url = "http://10.50.1.101:8086"


def CloseAllCases(Active_Records):
    client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)
    query_api = client.query_api()
    #write_api = write_client.write_api(write_options=SYNCHRONOUS)

    query_closeall = """ from(bucket: "OnondagaCountyiCAD")
  |> range(start: -2d)
  |> filter(fn: (r) => r["_measurement"] == "911Events")
  |> filter(fn: (r) => r["_field"] == "Status")
  |> filter(fn: (r) => r["record_ID"] != "PlaceholderID")"""
     

    suffix = (" or r[record_ID] != ")
    for i in range(len(Active_Records)):
        if i == 0:
            string = Active_Records[i]
        elif  i == (len(Active_Records) - 1):
            string = (string + Active_Records[i])
        elif i == len(Active_Records): 
            Var = 1  
        else: 
            string = (string + Active_Records[i] + suffix)
    query = query_closeall.replace("PlaceholderID", string)
    CloseAll = query_api.query(query, org="User-Space")

    
    

