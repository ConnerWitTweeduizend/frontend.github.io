a = input("Enter first number: ")
b = input("Enter operator (+ - * /): ")
c = input("Enter second number: ")
x = int(a)
y = int(c)
def func():
        if b == "+":
            print("output: ", x + y)
        elif b == "-":
            print("output: ", x - y)
        elif b == "*":
            print("output: ", x * y)
        elif b == "/":
            print("output: ", x / y)
        else:
            print("incorrect operator input.")
func()