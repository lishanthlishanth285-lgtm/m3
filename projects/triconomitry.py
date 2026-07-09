import math

ang = float(input("Type an angle (degrees): "))
rad = math.radians(ang)

sinx = math.sin(rad)
cosx = math.cos(rad)
tanx = math.tan(rad)
trico = input("Which one do you want to calculate? (sin, cos, tan): ")

if trico == "sin":
    print(f"The sine of {ang} degrees is: {sinx}")
elif trico == "cos":
    print(f"The cosine of {ang} degrees is: {cosx}")
elif trico == "tan":
    print(f"The tangent of {ang} degrees is: {tanx}")
else:
    print("Invalid option. Please choose 'sin', 'cos', or 'tan'.")