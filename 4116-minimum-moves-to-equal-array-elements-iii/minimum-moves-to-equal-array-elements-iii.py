
class Solution:
    def minMoves(self, nums):
        maximum = max(nums)

        count = 0

        for num in nums:
            count += maximum - num

        return count
