import json
import csv
import time
import io
import requests
import sys

truck = sys.argv[1]
start_time = sys.argv[2]
end_time = sys.argv[3]
token = sys.argv[4]
url = 'https://api.blackbuck.com/tracking-query/api/v1/entity/plot?entity='+str(truck)+'&start_time='+str(start_time)+'&end_time='+str(end_time)+'&stoppages=true&entity_type=TRUCK'
headers = {'content-type': 'application/json','authorization': 'token '+str(token)+''}
data = requests.get(url,headers=headers)
with open('data.json', 'w') as f:
    json.dump(data.json(), f)

# Opening JSON file and loading the data
# into the variable data
with open('data.json') as json_file:
    data = json.load(json_file)
    print(data)

gps_data = data['stoppages']

# now we will open a file for writing
data_file = open('data_file.csv', 'w')

# create the csv writer object
csv_writer = csv.writer(data_file)

# Counter variable used for writing
# headers to the CSV file
count = 0

for gps in gps_data:
    if count == 0:

        # Writing headers of CSV file
        header = gps.keys()
        csv_writer.writerow(header)
        count += 1

    # Writing data of CSV file
    csv_writer.writerow(gps.values())

data_file.close()

result = []
with open('data_file.csv') as f:
    data = csv.DictReader(f)

    for x in data:
        # x['Value3'] = float(x['entry']) + 1000
        x['entry_time_GMT']=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(x['entry_time']) / 1000))
        x['exit_time_GMT']=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(x['exit_time']) / 1000))
        result.append(x)

with open('output.csv', 'w+') as f:
    csv_writer = csv.DictWriter(f, fieldnames=result[0].keys())

    csv_writer.writeheader()
    csv_writer.writerows(result)
