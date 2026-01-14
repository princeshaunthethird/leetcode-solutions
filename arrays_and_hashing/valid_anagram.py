class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Step 1: If lengths are not equal, they cannot be anagrams
        if len(s) != len(t):
            return False

        # Step 2: Create a dictionary to count characters in s
        count = {}

        for char in s:
            count[char] = count.get(char, 0) + 1

        # Step 3: Subtract character counts using t
        for char in t:
            if char not in count:
                return False
            count[char] -= 1
            if count[char] < 0:
                return False

        # Step 4: If all counts match, it's a valid anagram
        return True
