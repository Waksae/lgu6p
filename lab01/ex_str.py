s = "Hello \"EASY\" Python"
print(s)
print(type(s))
s = """Hello,
"Easy" Python
"""
print(s)
##############################
# F-String
##############################
a = 2
b = 2000
c = a * b
print('c:', c)
print(f"c: {c} SUCCESS")
print(f"c: {c:f} SUCCESS")

print(f"{a} * {b} = {c}")
print(f"{a:.2f} * {b:.2f} = {c:.2f}")
print(f"{a:2.2f} * {b:2.2f} = {c:2.2f}")
print(f"{a:3.2f} * {b:3.2f} = {c:3.2f}")
print(f"{a:4.2f} * {b:5.2f} = {c:5.2f}")
print(f"{a:5.2f} * {b:5.2f} = {c:5.2f}")
print(f"{a:6.2f} * {b:8.2f} = {c:5.2f}")

a = "hello"
print(f"{a:_^15}")
print(f"{a:^15}")