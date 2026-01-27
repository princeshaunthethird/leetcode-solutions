from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        count = 0
        n = len(nums)

        # count how many times the order breaks
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                count += 1
                if count > 1:
                    return False

        # check circular (rotation) condition
        if count == 1 and nums[-1] > nums[0]:
            return False

        return True


print(Solution().check([1,2,3,4]))      # True
print(Solution().check([3,4,1,2]))      # True
print(Solution().check([2,1,3,4]))      # False
print(Solution().check([3,1,4,2]))      # False
print(Solution().check([1,1,1]))        # True
