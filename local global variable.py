marks=10
def scope():
    marks=5
    print(marks,"global or local variable")
scope()
print(marks,"globsl")
def gobalscope():
    print(marks,"certainly local?? or gobal??")
gobalscope()
