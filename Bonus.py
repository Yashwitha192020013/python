salary=float(input("Enter your salary: "))
if salary<=10000 and salary>2000:
    print("bonus=",salary*(5/100))
elif salary>10000:
    print("bonus=",salary*(7.5/100))
elif salary<=2000:
    years=int(input("Enter years of experience: "))
    if years<5:
              print("bonus=",salary*0.01)
    else:
        print("bonus=",salary*0.05)
else:
    print("invalid input")
