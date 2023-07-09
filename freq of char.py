def char_frequency(string):
    frequency = {}
    for char in string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency
input_string = "india"
frequency = char_frequency(input_string)
print("Character frequencies:")
for char, count in frequency.items():
    print(char, ":", count)
