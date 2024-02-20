import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

token = 'w04oO0vXp-RrUYE7Nj4Wqc9gR0c4KF0IQ9wfsqGQvP5bGt-KWgdYM6RYG4nw6VF_khZNEYaLT1dx1fAUTTMCWQ=='
org = "User-Space"
url = "http://10.50.1.101:8086"


def QueryDB(record_ID):
    client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)
    query_api = client.query_api()

    query_input =""" from(bucket: "Data3")
        |> range(start: -1d)
        |> filter(fn: (r) => r["_measurement"] == "911Events8")
        |> filter(fn: (r) => r["_field"] == "record_ID")
        |> filter(fn: (r) => r["_value"] == "PlaceholderID")
        |> last()
        |> yield(name: "_results") """
    query = query_input.replace("PlaceholderID", record_ID)
      
    records = query_api.query(query, org="User-Space")
    if len(records) == 0:
        Exist = 0
    else:
        Exist = 1
    return Exist

