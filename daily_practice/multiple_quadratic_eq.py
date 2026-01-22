import math


def solve_quad(a, b, c):
        if a == 0:
            print(f"the equation with a={a} is invalid")
            return
        Disc = b**2 - 4*a*c
        den = 2*a
        if Disc > 0:
            root1 = (-b + math.sqrt(Disc)) / (den)
            root2 = (-b - math.sqrt(Disc)) / (den)
            print(f"the root of the equation are real and {root1} and {root2}")


        elif Disc == 0:
            root = -b / (den)
            print (f"THE ROOT OF THE EQUATION is {root}")
            
        else:
            real_part = -b / (den)
            complex_root = math.sqrt(-Disc) / (den)
            print(f"The two roots are complex and they are {real_part:.2f}+{complex_root:.2f}i and {real_part}-{complex_root:.2f}i")
# another way of doing the output
            print(
            f"The roots are complex: "
            f"{real_part:.2f}+{complex_root:.2f}i and "
            f"{real_part:.2f}-{complex_root:.2f}i"
        )
            
    
a1 = float(input("Enter the value of a :"))
b1 = float(input("Enter the value of b :"))
c1 = float(input("Enter the value of c :"))
solve_quad(a1, b1, c1)

a2 = float(input("Enter the value of a : "))
b2 = float(input("Enter the value of b: "))
c2 = float(input("Enter the value of c: "))
solve_quad(a2, b2, c2)
