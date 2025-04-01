orders = [
    {
        "country": "USA",
        "customers": [
            {
                "customer_id": "C001",
                "orders": [
                    {"product": "Laptop", "quantity": 1, "unit_price": 1200},
                    {"product": "Mouse", "quantity": 2, "unit_price": 25}
                ]
            },
            {
                "customer_id": "C002",
                "orders": [
                    {"product": "Smartphone", "quantity": 1, "unit_price": 800}
                ]
            }
        ]
    },
    {
        "country": "Canada",
        "customers": [
            {
                "customer_id": "C003",
                "orders": [
                    {"product": "Laptop", "quantity": 2, "unit_price": 1150},
                    {"product": "Keyboard", "quantity": 1, "unit_price": 100}
                ]
            }
        ]
    }
]


# result = {
#     "C001": {
#         "country": "USA",
#         "products": ["Laptop", "Mouse"],
#         "total_amount": 1250  # (1 x 1200) + (2 x 25)
#     },
#     "C002": {
#         "country": "USA",
#         "products": ["Smartphone"],
#         "total_amount": 800
#     },
#     "C003": {
#         "country": "Canada",
#         "products": ["Laptop", "Keyboard"],
#         "total_amount": 2400  # (2 x 1150) + (1 x 100)
#     }
# }

def order_by_customers(orders):
    result={}
    for i in range(len(orders)):
        CT = orders[i]['country']
        for j in range(len(orders[i]['customers'])):
            ID = orders[i]['customers'][j]["customer_id"]
            result[ID] = {}
            result[ID]["country"] = CT
            result[ID]["products"]= []
            result [ID]["total_amount"] = 0
            for k in range(len(orders[i]['customers'][j]["orders"])):
                PN = orders[i]['customers'][j]["orders"][k]["product"]
                Q = orders[i]['customers'][j]["orders"][k]["quantity"]
                P = orders[i]['customers'][j]["orders"][k]["unit_price"]
                result[ID]["products"].append (PN)
                result[ID]["total_amount"] += (Q*P)

    return result
print(order_by_customers(orders))



