from csv import reader
import json
import requests

with open('/Users/thottarajasekar/Downloads/hold_in.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    for row in csv_reader:
        print(row[0])
        txn_id = row[0]
        url = "https://etoll.idfcbank.com/dimtspay_services_web/fetchTxnStatus"
        json_data = json.dumps({"agencyId": "62497", "txnId": txn_id})
        auth_token = 'Basic MjEwOTkyOjEyMzQ1Ng=='
        headers = {"Content-Type": "application/json", 'Authorization': auth_token}
        r = requests.post(url, data=json_data, headers=headers)
        result = r.json()
        print(r.status_code)
        print(r.json())
        txn = result['txnId']
        res = result['resCode']
        print(type(res))
        print("the transaction response is:", txn, res)
        if res == '700':
            print("the transaction is successful")
            with open("success.csv",'w') as file:
                file.write(txn, res)
        elif res == '710':
            print("The transaction is failure")
            url_mark = 'https://api-fms.blackbuck.com/payments/api/hold/remove/txnfailure'
            txn_json_data = json.dumps({"txn_id": txn_id})
            auth_token = 'Token :ek8sg5oqlbxfysbmxh0g0hf6o7f7qinp'
            headers = {"Content-Type": "application/json", 'Authorization': auth_token}
            ro = requests.post(url=url_mark, data=txn_json_data, headers=headers)
            ro_msg = ro.json()
            print(ro_msg['data']['message'])
            print(txn_json_data)
