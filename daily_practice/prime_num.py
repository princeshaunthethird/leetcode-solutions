num = int(input("Enter a number"))
if num <= 1:
    print(f"The number {num} is not a prime number")
else:
    flag = True
    for i in range(2, int(num**0.5) +1):
        if(num % i == 0 ):
            flag = False
            break
    if flag:
        print(f"the number {num} is a prime number")
    else:
        print(f"The number {num} is not a prime number")