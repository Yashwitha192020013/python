X = [[1,7,4],
    [4 ,5,6],
    [7 ,4,9]]
Y = [[3,8,1],
    [6,7,9],
    [4,5,12]]

result = [[0,0,0],
         [0,0,0],
         [0,0,0]]
for i in range(len(X)):
   for j in range(len(X[0])):
       result[i][j] = X[i][j] + Y[i][j]
for r in result:
   print(r)
