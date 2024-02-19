import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

token = 'w04oO0vXp-RrUYE7Nj4Wqc9gR0c4KF0IQ9wfsqGQvP5bGt-KWgdYM6RYG4nw6VF_khZNEYaLT1dx1fAUTTMCWQ=='
org = "User-Space"
url = "http://10.50.1.101:8086"
write_client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)

def Get_Case_Status(record_ID)
    query_api = client.query_api()

    query = ""from(bucket: "Data2")
        |> range(start: -10m)
        |> filter(fn: (r) => r["record_ID"] == record_ID)""
    tables = query_api.query(query, org="User-Space")

    for table in tables:
        for record in table.records:
            print(record)

    if location:
            return Status = 1
        else:
            return Status = 0