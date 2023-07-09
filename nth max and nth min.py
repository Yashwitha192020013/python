a=[]
size=int(input("Enter size of list: "))
for i in range (0,size):
    i=int(input("Enter elements: "))
    a.append(i)
a.sort()
print(a)
print("Enter the nth maximum")
print("Enter th mth minimum")
print("nth Maximum element= ",(a[size-1]))
print("nth minimum element= ",(a[size+1]))
