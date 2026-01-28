lower = int(input("Enter the lower limit of the range"))
upper = int(input("Enter the upper limit of the range"))

for num in range (lower , upper + 1):
    original = num
    digits = len(str(num))
    total = 0
    
    while original >0:
        digit = original % 10
        total += (digit ** digits)
        original = original // 10
        
    if total == num:
        print(f"The number {num} is an armstrong number")
        