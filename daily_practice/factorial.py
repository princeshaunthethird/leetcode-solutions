num = int(input("Enter a number to know its factorial: "))
if num < 0:
    print(f"The number {num} is not a valid number as it is invalid")
elif num == 0:
    print(f"The number {num} has a factorial value of 1")
else:
    factorial = 1
    for i in range(1,num+1):
        factorial *= i
    print (f"the factorial of the {num} is {factorial}")