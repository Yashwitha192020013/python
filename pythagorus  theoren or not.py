ab=int(input("Enter Ab value: "))
bc=int(input("Enter BA value: "))
ca=int(input("Enter CA value: "))
a=ab*ab
b=bc*bc
c=ca*ca
print("To Prove CA^2=AB^2+BA^2")
if c==a+b:
    print("It is a Pythagoras Theorem")
else:
    print("It is Not a Pythagoras Theorem")
