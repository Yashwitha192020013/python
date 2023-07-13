keys = ['Tens', 'Hundreds', 'Thousands']
values = [10, 200, 3000]
res_dict = dict()
for i in range(len(keys)):
    res_dict.update({keys[i]: values[i]})
print(res_dict)
