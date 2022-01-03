from csv import reader
import json
import requests
import requests as requests

with open('/Users/thottarajasekar/Downloads/sales_codes.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    for row in csv_reader:
        print(row[0])
        sales_code = row[0]
        coupon_code = row[1]
        plan_id = row[2]
        url = "https://api-fms.blackbuck.com/fmsiot/api/v2/coupon/config"
        json_data = json.dumps({"coupon_code": coupon_code, "activation_date": "2022-01-01", "expiration_date": "2022-12-31",
                                "type": "PART_PAY_DISCOUNT", "part_pay":0, "discount":500, "sales_code": sales_code})
        auth_token = 'Token :ek8sg5oqlbxfysbmxh0g0hf6o7f7qinp'
        headers = {"Content-Type": "application/json", 'Authorization': auth_token}
        r = requests.post(url, data=json_data, headers=headers)
        result = r.json()
        print(r.json())
        refid = result['id']
        print(r.status_code)
        if r.status_code == 200:
            url_mark = "https://api-fms.blackbuck.com/fmsiot/api/v1/map/coupon_gps_plan"
            in_json_data = json.dumps({"couponConfigId": refid,"gpsPlanId": plan_id})
            headers = {"Content-Type": "application/json", 'Authorization': auth_token}
            plan = requests.post(url=url_mark, data=in_json_data, headers=headers)
            print(plan.json())
            result = plan.json()
            output = json.dumps(result)
            with open("success_map.csv",'w') as file:
                file.write(output)
        elif r.status_code != 200:
            print("response data not loaded")
