listnum=[]
n=int(input("Enter number of elememts"))
for i in range(0,n):
      ele=int(input())
      listnum.append(ele)
print(listnum)
even=[]
odd=[]
for i in listnum:
    if(i%2==0):
        even.append(i)
    else:
        odd.append(i)
print("Even list",even)
print("Odd list",odd)
