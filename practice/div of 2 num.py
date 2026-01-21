num1 = float(input("Enter a number for division"))
num2 = float(input("Enter the second number for division"))
div_res = num1/ num2
if num2 == 0:
    print("Divisor cannot be 0")
else:
    print(f"div of {num1} / {num2} is {div_res}")