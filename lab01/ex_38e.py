products = [
    {
        "category": "Electronics",
        "items": [
            {"name": "Laptop", "price": 1200, "stock": 5},
            {"name": "Smartphone", "price": 800, "stock": 10}
        ]
    },
    {
        "category": "Home Appliances",
        "items": [
            {"name": "Vacuum Cleaner", "price": 150, "stock": 7},
            {"name": "Air Conditioner", "price": 500, "stock": 3},
            {"name": "Air Cleaner", "price": 900, "stock": 4}
        ]
    }
]

# result = {
#     "Laptop": {"price": 1200, "stock": 5},
#     "Smartphone": {"price": 800, "stock": 10},
#     "Vacuum Cleaner": {"price": 150, "stock": 7},
#     "Air Conditioner": {"price": 500, "stock": 3}
# }


# def convert_data(products):
#     for i in products:
#         del products[i]["category"]
#         for j in products[i]:
#             Name = products[0]['items'][0]['name']
#             del products[i]['items'][j]['name']
#             print(f'"{Name}": ',products[0]['items'][0])

def convert_data(products):
    pass
    result_d = {}
    Name = " "
    for i in range(len(products)):
        del products[i]["category"]
        for j in range(len(products[i]['items'])):
            Name = products[i]["items"][j]["name"]
            del products[i]["items"][j]["name"]
            info = products[i]["items"][j]
            result_d[Name]=info
    return result_d

print(convert_data(products))
# import json

# print(json.dumps(convert_data(products),indent=2))