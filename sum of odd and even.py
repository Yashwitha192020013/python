test_list = [1,5,4,8,9]
print("The original list is : " + str(test_list))
 
odd_sum = 0
even_sum = 0
 
for sub in test_list:
    for ele in str(sub):
         
        if int(ele) % 2 == 0:
            even_sum += int(ele)
        else:
            odd_sum += int(ele)
print("Odd digit sum : " + str(odd_sum))
print("Even digit sum : " + str(even_sum))
