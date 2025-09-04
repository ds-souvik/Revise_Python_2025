"""Use dictionaries in case of repeated case using if else or match case

To learn this we will simulate a design similar to that in the industry"""

payments = [
    {"id": 1, "total_sum": 1000, "coupon": "P20"}, 
    {"id": 2, "total_sum": 1200, "coupon": "P30"}, 
    {"id": 3, "total_sum": 1250, "coupon": "F10"}
]

discounts = {"P20": (0.2,0), "P30": (0.3, 0), "F10": (0, 10)}

output_list=[]

for payment in payments:
    amt, code = payment["total_sum"], payment["coupon"]
    output_list.append(f"{payment["id"]} needs to pay {amt * (1-discounts[code][0]) - discounts[code][1]}")

print(output_list)