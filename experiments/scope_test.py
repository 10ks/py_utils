def fffunc():
    print(i)

def func2(param1):
    print(param1)
    # print(y)  # NameError: name 'y' is not defined
    print(x)

def func1():
    y = 30
    func2(20)



for a in range(10):
    print(a)
    for i in range(4):
        print(i)

print("---")
print(a)
print(i)
fffunc()

x = 10
func1()

