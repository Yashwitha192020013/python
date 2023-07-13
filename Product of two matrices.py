X = [[1,8,3],
    [3,5,6],
    [9,8,3]]

Y = [[5,2,1,2],
    [6,7,1,0],
    [4,5,5,1]]

result =[ [0,0,0,0],
          [0,0,0,0],
          [0,0,0,0]]

for i in range(len(X)):
   for j in range(len(Y[0])):
       for k in range(len(Y)):
           result[i][j] += X[i][k] * Y[k][j]
for r in result:
   print(r)
