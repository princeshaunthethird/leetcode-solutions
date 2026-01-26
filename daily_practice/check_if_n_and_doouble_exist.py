def checkIfExist(arr):
    seen = set()

    for i in arr:
        if (2 * i in seen) or (i % 2 == 0 and i // 2 in seen):
            return True
        seen.add(i)

    return False

arr = [10, 2, 3, 6, 5, 9]
print(f"{checkIfExist(arr)}")


#This soln works fir most outputs except a few cases
#       n = len(arr)
#
#       for i in range(n):
#          for j in range(n):
#                if i != j and arr[i] == 2 * arr[j]:
#                    return True
#
#       return False