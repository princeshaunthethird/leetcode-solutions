num1 = int(input("Enter the first number to check the LCM"))
num2 = int(input("Enter the second number whoes lcm is required"))

def LCMCAL(x,y):
    if x> y:
        greater = x
    else:
        greater = y
    
    while True:
        if((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater +=1
    return lcm

print(f"the LCM of the two numbers are {LCMCAL(num1,num2)}")