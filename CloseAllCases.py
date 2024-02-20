import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

token = 'w04oO0vXp-RrUYE7Nj4Wqc9gR0c4KF0IQ9wfsqGQvP5bGt-KWgdYM6RYG4nw6VF_khZNEYaLT1dx1fAUTTMCWQ=='
org = "User-Space"
url = "http://10.50.1.101:8086"


def CloseAllCases():
    client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)
    query_api = client.query_api()
    
    query_closeall = """ from(bucket: "Data3")
        |> range(start: -30d)
        |> filter(fn: (r) => r._measurement == "911Events8" and r._field == "record_ID")
        |> map(
            fn: (r) => ({r with
                Status: if r.Status == "Open" then
                    "Closed"
                    else
                    "Closed",
            }),
        ) """

    CloseAll = query_api.query(query_closeall, org="User-Space")
       

    

