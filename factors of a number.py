num=int(input("Enter a number: "))
num = int(num)
print("Factors of", num)
i = 1
while i<=num:
    if num%i==0:
        print(i)
    i = i+1
