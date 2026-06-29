def add(a, b):
    a + b
    sum = a + b
    print(f"the sum of {a} and {b} is: {sum}")

def sub(a, b):
    a - b
    sum = a - b
    print(f"the difference of {a} and {b} is: {sum}")

def mul(a, b):
    a * b
    sum = a * b
    print(f"the product of {a} and {b} is: {sum}")

def div(a, b):
    a / b
    sum = a / b
    print(f"the quotient of {a} and {b} is: {sum}")

ans = input("select ur operattion: \n 1. addition \n 2. subtraction \n 3. multiplication \n 4. division \n enter your choice: ")

a = int(input("enter the first number: "))
b = int(input("enter the second number: "))

if ans == '1':
    add(a, b)
elif ans == '2':
    sub(a, b)
elif ans == '3':
    mul(a, b)
elif ans == '4':
    div(a, b)
