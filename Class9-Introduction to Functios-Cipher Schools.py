#Introduction

x = 6
x = "Amrit"
x = 2.5
x = print



def show_loading():
    for i in range(3):
        print("loading...")


a = 5
b = 7

print(a + b)
show_loading()

print(a - b)
show_loading()

print(a * b)
show_loading()



#Functions can take parameters

def sheldon_knock():
    for i in range(5):
        print("knock knock knock Amrit")
sheldon_knock()



def sheldon_knock(name, times = 3):
    for i in range(times):
        print("knock knock knock", name)
sheldon_knock("Amrit", 100)





#Return statements

def add(a,b):
    return a + b
a = add(1,2)
print(a)

