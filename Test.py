import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS


token = 'w04oO0vXp-RrUYE7Nj4Wqc9gR0c4KF0IQ9wfsqGQvP5bGt-KWgdYM6RYG4nw6VF_khZNEYaLT1dx1fAUTTMCWQ=='
org = "User-Space"
url = "http://10.50.1.101:8086"

Active_Records = ['8934e651627165541f049fb62db56a7bcf3fa1aa973b5fa588190b70ff7c900d',
 'e5e378cc110a1bc30338020624202991272b42c3f161ef3b6e0f9a0e603f6f25',
 '83d7ccbf5e97c2a81f10ad747af6635b50a368c88a6d9fe2e7fdfbdb4a951ee8',
 'e554616a9d0ef0789287bd44cf601e217e4c960488016afe2304e2d561fca8f1',
 '1e5c62243debd3ded6a0843a34e0dde80e5e14cfd38a4dea3b5bcf7df996328f',
 '8a961abb2aed46c4ff408082304d9d6342bc17dfbb7b66acd7d2a01e664ca46b',
 'da60e23f429493370098550eafdc4b38e90964ed79fdc5cc67fe1c6ebb29af19',
 '526684d16bde7bb1a6206cedac1a52dccbcee7a960d509911095e98621c3b345',
 '6e23c1490134d8ddb660673194a2c321803c851fe7756a57e4ef25848f43797c',
 'f17341f09accf169a3ad0ecf593942c4184922db8da86025bff3616400d92a56',
 'dbebaab36b2d016d42a3b0acc7cdbde58df4fffd74c3e131e4943cd10a171e96',
 'daefd4bdb50672922bc66fca70ad8869405e47e71f101c18dea134959f082b4f',
 'a0bcca9a0bb47843f164ec822a1b99af6e17b2fed4bd1b2241fe692dffc4cee2',
 '3fcd3c5a3a8285e5bf538792925cb547f6cbf11d46ce64f6053875c22b7a8746',
 '98bc199c386ff6248f7b2cd7e2ff45173e849c715867c68f7150f99645474919',
 '030b55e756d58bc94cd14266c04118dc3e4d8a2b9310e63a5dbf0e37134ea4e3',
 'c87cc5f8c1f5511643da274caed396a1b8d873ccdfe8df6a1f647038a825622d',
 '567f32f624842f0cd03f39deb5138408b6a7957d501b1de83a37f311a8f1d4aa',
 '936281bd7a539925322870421a27e25e34edb879ac937d201d749234bfde92de']

client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)



query_api = client.query_api()

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
    



client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)
write_api = client.write_api(write_options=SYNCHRONOUS)
query_api = client.query_api()
bucket="OnondagaCountyiCAD"

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
    #write_api.write(bucket=bucket, org="User-Space", record=point)

