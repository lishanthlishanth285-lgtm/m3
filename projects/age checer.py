try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError
    elif age == float:
        raise ValueError
    elif age == str:
        raise ValueError
    elif age > 100:
        raise ValueError
except ValueError:
    print("problem: You have entered a miss matching value")
