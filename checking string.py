open_list = ["[", "{", "("]
close_list = ["]", "}", ")"]
def check(myStr):
    staCheck = []
    for i in myStr:
        if i in open_list:
            staCheck.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if ((len(staCheck) > 0) and
                    (open_list[pos] == staCheck[len(staCheck) - 1])):
                staCheck.pop()
            else:
                return "Unbalanced"
    if len(staCheck) == 0:
        return "Balanced"
    else:
        return "Unbalanced"

string = "[[]]"
print(string, "-", check(string))

string = "{}"
print(string, "-", check(string))

string = "(()){"
print(string, "-", check(string))
