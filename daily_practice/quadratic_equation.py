import math

a = int(input ("Enterr the value for a = "))
b= int(input("Enter the value for b = "))
c = int(input("Enter the value for c = "))
# calculating ax^2 + bx + c = 0
#here the main things is that if a == 0 then it is not a quadratic equation
# so now we can get the solution based on the discriminant
if a == 0:
    print("the equation is not a quadratic equation")
else:
    D = b**2 - 4*a*c

    if D > 0:
        root1 = (-b+ D**0.5) / (2*a)
        root2 = (-b - math.sqrt(D)) / (2*a)
        print(f"the roots are {root1} and {root2}")
        
    elif D==0:
        root = -b / (2*a)
        print(f"The  only root is {root}")
        
    else:
        real_part = -b / (2*a)
        img_part = (math.sqrt(-D)) / (2*a)
        print(f"The roots are {real_part}+{img_part}i and {real_part}-{img_part}i")
        