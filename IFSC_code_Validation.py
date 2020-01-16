#!/usr/b/python3
import json

import requests

ifsc_codes = []
with open('/Users/thotarajasekhar/Downloads/44_ifsc.csv', "r") as inf:
    for line in inf:
        ifsc_codes.append(line.strip('\n'))
    # print(ifsc_codes)
for url in ifsc_codes:
    response = requests.get("https://ifsc.razorpay.com/{}".format(url))
    data = response.json()
    # print(data)
    if data == 'Not Found':
        with open('44_NotFound_IFSC.txt', 'a') as the_file:
            the_file.write(url)
            the_file.write("\n")
    else:
        print(data["IFSC"])
        pass
