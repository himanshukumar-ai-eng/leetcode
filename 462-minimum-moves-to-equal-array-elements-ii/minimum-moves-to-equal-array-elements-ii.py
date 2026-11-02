class Solution:
    def minMoves2(self, nums):
        nums.sort()
        median = nums[len(nums)//2]
        count = 0
        for num in nums:
            count += abs(num - median)
        return count
       