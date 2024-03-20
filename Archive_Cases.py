import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

token = 'w04oO0vXp-RrUYE7Nj4Wqc9gR0c4KF0IQ9wfsqGQvP5bGt-KWgdYM6RYG4nw6VF_khZNEYaLT1dx1fAUTTMCWQ=='
org = "User-Space"
url = "http://http://syr-incidents.koniers.net:8086"


def SortInactive(Active_Records):
    client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)

    query_api = client.query_api()
    if Active_Records == []:
      query = """from(bucket: "OnondagaCountyiCAD")
      |> range(start: -10d)
      |> filter(fn: (r) => r._measurement == "911Events")"""
      
    else:
      query = """from(bucket: "OnondagaCountyiCAD")
      |> range(start: -10d)
      |> filter(fn: (r) => r._measurement == "911Events")
      |> filter(fn: (r) => PlaceholderID )"""
     
      Query_Text = (""" """)
      for i in range(len(Active_Records)):
        if i == 0:
          temptext = (""" r["record_ID"] !=  "Placeholder" """)
          temptext = temptext.replace("Placeholder", Active_Records[i])
          Query_Text += (temptext)
        else:
          temptext = (""" or r["record_ID"] !=  "Placeholder" """)
          temptext = temptext.replace("Placeholder", Active_Records[i])
          Query_Text += (temptext)
      query = query.replace("PlaceholderID", Query_Text)

    return query


def ChangeStatus(query):
  client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)
  write_api = client.write_api(write_options=SYNCHRONOUS)
  query_api = client.query_api()
  bucket="OnondagaCountyiCAD"
  if query == """from(bucket: "OnondagaCountyiCAD")\n    |> range(start: -10d)\n    |> filter(fn: (r) => r._measurement == "911Events")\n    |> filter(fn: (r) =>   ) """:
    query = """ from(bucket: "OnondagaCountyiCAD")\n    |> range(start: -10d)\n    |> filter(fn: (r) => r._measurement == "911Events") """
  else:
    query = query
  
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
        .time(Time_get)
        )
      write_api.write(bucket=bucket, org="User-Space", record=point)

