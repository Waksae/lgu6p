A = [ [1, 0, 1],
      [0, 2, 0]]

B = [ [2, 3],
      [0, 1],
      [1, 1] ]

C = []

for i in range(len(A)):                      # 행렬 A의 행 개수 (전체 행 번호 i)
    C.append([])                                 # 행렬 C 내 새로운 행(i) 생성
    for j in range(len(B[0])):                   # 행렬 B의 열 개수
        C[i].append(0)                               # 행렬 C i행 내 새로운 열(j) 생성 
        for k in range(len(B)):                      # 행렬 B의 열 개수 (전체 열 번호 j)
            C[i][j] += (A[i][k] * B[k][j])               # 행렬 C의 i행 j열 내적연산
    print(C[i])                                  # 행렬 C의 i행 출력
C = [[0,0],[0,0]]
row = len(A)
col = len(B[0])
for i in range(row):
    for j in range(col):
        for k in range(len(B)):
            C[i][j] += (A[i][k] * B[k][j])
    print(C[i])    