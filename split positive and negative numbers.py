Num = []
Positive = []
Negative = []
Number = int(input("Enter number of elements: "))
for i in range(1, Number + 1):
    value = int(input("enter elements : "))
    Num.append(value)

for j in range(Number):
    if(Num[j] >= 0):
        Positive.append(Num[j])
    else:
        Negative.append(Num[j])
print("Element in positive list is : ", Positive)
print("Element in negative list is : ", Negative)
