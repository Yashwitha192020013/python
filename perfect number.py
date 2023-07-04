num=int (input("Enter the number:"))
sum_f=0
for i in range(1,num):
   if(num%i==0):
    sum_f=sum_f=i
if(sum_f==num):
         print(num," is a perfect number")
else:
         print(num," is not a perfect number")
