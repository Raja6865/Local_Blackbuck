#!/usr/bin/python
import requests
url='https://api-fms.blackbuck.com/fms/api/admin/blacklist?MODE=BOTH'
auth_token = 'Token :ek8sg5oqlbxfysbmxh0g0hf6o7f7qinp'
headers = {"Content-Type": "application/json", 'Authorization': auth_token}
r=requests.get(url,headers=headers)
print(r.status_code)
print(r.json())
