a=[]
size=int(input("Enter size of list: "))
for i in range (0,size):
    i=int(input("Enter elements: "))
    a.append(i)
a.sort()
print(a)
print("Maximum element= ",(a[size-1]))
print("Second maximum element= ",(a[size-2]))
