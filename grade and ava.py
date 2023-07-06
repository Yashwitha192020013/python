mark1=int(input("sub1:"))
mark2=int(input("sub2:"))
mark3=int(input("sub3:"))
mark4=int(input("sub4:"))
mark5=int(input("sub5:"))
sum=mark1+mark2+mark3+mark4+mark5
avg=sum/5
print("The average marks obtained by the student is",avg)
if avg>90:
    print("Grade of the student is S")
elif avg>80:
    print("Grade of the student is A")
elif avg>70:
    print("Grade of the student is B")
elif avg>60:
    print("Grade of the student is C")
elif avg>50:
    print("Grade of the student is D")
else:
    print("Sorry,You failed")
