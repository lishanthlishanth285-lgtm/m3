try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    div = num1/num2
    print(div)
except ZeroDivisionError:
    print("You cannot divide by zero")
except SyntaxError:
    print("You have entered a formating errors")
except ValueError:
    print("You have entered a miss matching value")
except:
    print("You have entered a wrong input")
