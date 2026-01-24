"""
Prime Number Challenge

Requirements:
    - Take an integer n from the user
    - Determine whether n itself is a prime number
    - Print all prime numbers between 2 and n (inclusive)
    - Print how many prime numbers were found
"""


def prime_num(num):
        if num <= 1:
            print(f"The number {num} is not a prime number")
            return False
        else:
            for i in range(2, int(num**0.5)+1):
                if(num % i  == 0):
                    return False
            return True
                
n = int(input("Enter a number"))
if prime_num(n):
            print(f"the number {n} is a prime number")
else:
    print(f"the number {n} is not a prime number")
    
prime_list = []
for j in range(2,n+1):
    if prime_num(j):
        prime_list.append(j)
        
print(f"The prime numbers between 2 and {n} are")
print(f"{prime_list}")
print(f"the numbers of elements are {len(prime_list)} ")