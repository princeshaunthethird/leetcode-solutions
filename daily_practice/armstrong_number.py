num = int(input("Enter an integer"))
orignal = num
digits = len(str(num))
total = 0

while num >0:
    digit = num % 10
    total += (digit ** digits)
    num= num // 10
    
if total == orignal:
    print(f"The number {orignal } is an armstrong number")
else:
    print(f"The number {orignal} is not an armstrong number")