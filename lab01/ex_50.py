import random
class Linear:
    def __init__(self, in_feature, out_feature):
        self.in_feature = in_feature
        self.out_feature = out_feature
        self.weight = []
        self.bias = []
        for i in range(in_feature):               
            self.weight.append([])                              
            for j in range(out_feature):                 
                self.weight[i].append(random.random())
        for j in range(out_feature):
            self.bias.append(random.random())
                         
    def matmul(self, A, B):
        row = len(A)
        col = len(B[0])
        C=[]
        for i in range(row):
            C.append ([])
            for j in range(col):
                C[i].append (0)
        for i in range(row):
            for j in range(col):
                for k in range(len(B)):
                    C[i][j] += (A[i][k] * B[k][j])
        return C
    
    def forward(self,x):
        Z = self.matmul(x, self.weight)
        Y = []
        for i in range(len(Z)):                        # 
            for j in range(i+1):
                Z[i][j]= Z[i][j] + self.bias[j]
        return Z

linear = Linear(3, 2)
x = [ [1,2,3],
      [4,5,6] ]
print(linear.weight)
print(linear.bias)
print(linear.matmul(x,linear.weight))
print(linear.forward(x))
# print(linear.forward(x)) # 결과는 2행 2열로 나오면 된다.

#################################3
# 정답 확인용
import numpy as np
x_np = np.array(x)
W_np = np.array(linear.weight)
b_np = np.array(linear.bias)

y_np = np.dot(x_np,W_np) + b_np

print(W_np)
print(b_np)
print(np.dot(x_np,W_np))
print(y_np)
