num = int(input("Enter the value to which you need the fibonachi series"))
n1,n2 = 0, 1
for i in range(num):
    print(n1)
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    