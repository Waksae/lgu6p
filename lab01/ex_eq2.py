x = float(input('{:>9}'.format("x= ")))
mu = float(input('{:>9}'.format("mu= ")))
sig = float(input('{:>9}'.format("sigma= ")))
fx1= ( sig * 2.506 )
e = 2.718
fx2 = (x - mu)
fx3 = sig**2
fx4 = - ( fx2**2 ) / (2 * fx3)
fx = e**fx4 / fx1
print(fx)