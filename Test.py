import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

token = 'w04oO0vXp-RrUYE7Nj4Wqc9gR0c4KF0IQ9wfsqGQvP5bGt-KWgdYM6RYG4nw6VF_khZNEYaLT1dx1fAUTTMCWQ=='
org = "User-Space"
url = "http://10.50.1.101:8086"

client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)



query_api = client.query_api()

query = """from(bucket: "OnondagaCountyiCAD")
 |> range(start: -10d)
 |> filter(fn: (r) => r._measurement == "911Events")
 |> filter(fn: (r) => r["record_ID"] != "PlaceholderID" )"""


tables = query_api.query(query, org="User-Space")

for table in tables:
  for record in table.records:
    Agency_get = record.values.get('Agency')
    record_ID_get = record.values.get('record_ID')
    DateandTime_get = record.values.get('Date/Time')
    IncidentType_get = record.values.get('Incident Type')
    CityJurisdiction_get = record.values.get('City Jurisdiction')
    Lat_get = record.values.get('Latitude')
    Long_get = record.values.get('Longitude')
    Time_get = record.values.get('_time')
    point = (
        Point("911Events")
        .field("Status", "Closed")
        .tag("record_ID", record_ID_get)
        .tag("Date/Time", DateandTime_get)
        .tag("Agency", Agency_get)
        .tag("Incident Type", IncidentType_get)
        .tag("City Jurisdiction", CityJurisdiction_get)
        .tag("Latitude", Lat_get)
        .tag("Longitude", Long_get)
        .time("_time", Time_get)
        )
    #list = list.append(point)
    write_api.write(bucket=bucket, org="User-Space", record=point)

