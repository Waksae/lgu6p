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

# def order_by_customers(orders):
result={}
for order in orders:
    CT = order['country']
    for customer in order['customers']:
        ID = customer["customer_id"]
        result[ID]={}
        result[ID]["country"]=CT
        result[ID]["products"]=[]
        result[ID]["total_amount"] = 0
        for info in customer["orders"]:
            PN = info["product"]
            Q = info["quantity"]
            P = info["unit_price"]
            result[ID]["products"].append (PN)
            result[ID]["total_amount"] += ( Q * P )
print(result)