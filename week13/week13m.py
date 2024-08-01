from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
from datetime import datetime

# Configuration
url = "http://localhost:8086"
username = "root"
password = "emre1234"
org = "emre"
bucket = "emre"

# Initialize the client with username and password
# client = InfluxDBClient(url=url, username=username, password=password, org=org)
client = InfluxDBClient(url=url, org=org)

# Verify connection and list available buckets
try:
    buckets_api = client.buckets_api()
    buckets = buckets_api.find_buckets().buckets

    print("Available buckets:")
    for b in buckets:
        print(f"- {b.name}")

    # Check if the specified bucket exists
    if bucket not in [b.name for b in buckets]:
        raise ValueError(f"Bucket '{bucket}' does not exist.")

    # Create a point and write it to the bucket
    write_api = client.write_api(write_options=SYNCHRONOUS)
    point = Point("measurement_name")\
        .tag("location", "store")\
        .field("temperature", 25.3)\
        .field("sound", 5000)\
        .time(datetime.utcnow(), WritePrecision.NS)

    write_api.write(bucket=bucket, org=org, record=point)
    print("Data written successfully")

except ValueError as ve:
    print(f"ValueError: {ve}")
except Exception as e:
    print(f"An error occurred: {e}")
