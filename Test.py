import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

token = 'w04oO0vXp-RrUYE7Nj4Wqc9gR0c4KF0IQ9wfsqGQvP5bGt-KWgdYM6RYG4nw6VF_khZNEYaLT1dx1fAUTTMCWQ=='
org = "User-Space"
url = "http://10.50.1.101:8086"



client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)
query_api = client.query_api()


    
Active_Records = ['5007d916615869dd26b33e399ed7f5049703b619610c475d178a2a38310afcbb',
 '015774df8f73010d25d01af9d7ca8add67fe0ee7f78c3450b85724417f1d1565',
 '524adcfa109188bf44933c1799d035480a2b52b9058febd1e370201aafad2a82',
 'ba1e8f398771f155e056dcbe25edd7c301fd01ec5d7d410894260db8e491d7c4',
 '13044711d7a967c91d1e2df1676bcb1948ccbd256ed52f0fc2d73eaf4e81f8cb',
 'a2f20e7b1316e42bd408b03c5c01e60c2888dde00a4bd3fb92046b6b3bb2efa5']

Records = Active_Records
    
query_input = """ from(bucket: "Data3")
    |> range(start: -30d)
    |> filter(fn: (r) => r._measurement == "911Events8" and r._field == "record_ID"
    |> map(
        fn: (r) => ({r with
            Status: if r._value == PlaceholderID
                "Open"
                else
                "Closed",
        }),
    ) """


suffix = """ == or """
for i in range(len(Records)):
    if i == 0:
        entry = (Records[i] + suffix) 
    elif i == len(Records):
        entry.__add__(Records[i] + "then") 
    else:
        entry.__add__(Records[i] + suffix)    
query = query_input.replace("PlaceholderID", entry)
      
remap = query_api.query(query, org="User-Space")
Outcome = "Success"
return(Outcome)
    

