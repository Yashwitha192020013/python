def swapPositions(lis, pos1, pos2):
    temp=lis[pos1]
    lis[pos1]=lis[pos2]
    lis[pos2]=temp
    return lis
List = [1,10,100,1000]
print(List)
pos1, pos2 = 2, 3
print(swapPositions(List, pos1-1, pos2-1))
