test_str="Are all alloys as abundant as aluminium?"
print("Original string: "+str(test_str))
letter="a"
res=0
x=test_str.split()
for i in x:
    if(i.find(letter)!=1):
        res+=1
print("Word count: "+str(res))
