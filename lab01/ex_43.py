# def op(x, z, y):
#     return (x + y)*z

# x = 2
# y = 3
# z = 4

# print(op(x,z,y))
# print(op(x,y,z))

# print(op(x=x,y=y,z=z))
# print(op(x,y=y,z=z))

def print_all(*args,**kwargs):
    print(args)
    print(kwargs)

print_all(1,2,3,4,5,6,x=100,y=200,z=300)