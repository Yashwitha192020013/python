list1=[1,2,3,4,5,1,2,3]
list2=[]
count=len(list1)
for i in list1:
    if i not in list2:
        list2.append(i)
        count -=1
print(list2)
print("Number of duplicates", count)
list4=[]
for i in range(count):
    list4.append('_')
result=list2+list4
print(result)
