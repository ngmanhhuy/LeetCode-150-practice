class Solution:
    def removeElement(self, nums, val) -> int:
        k = 0
        for i in range(0, len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k

#test
nums = [3, 2, 2, 3]
val = 3
k = Solution().removeElement(nums, val)
print(k)
print(nums)

