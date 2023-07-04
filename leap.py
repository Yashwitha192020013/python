Year=int(input("Enter the Year"))
if (Year%4==0 or Year%400==0) and (year%100==0):
  print(Year,"leap Year")
else:
    print(Year,"not a leap Year") 
