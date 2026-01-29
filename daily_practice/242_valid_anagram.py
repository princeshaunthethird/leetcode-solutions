def isAnagram(s, t):
    if len(s) != len(t):
        return False

    count = {}

    for ch in s:
        if ch in count:
            count[ch] += 1
        else:
            count[ch] = 1

    for ch in t:
        if ch not in count:
            return False
        count[ch] -= 1
        if count[ch] < 0:
            return False

    return True

s1 = "anagram"
t1 = "nagaram"

s2 = "rat"
t2 = "car"

print("Test 1:", isAnagram(s1, t1))
print("Test 2:", isAnagram(s2, t2))
