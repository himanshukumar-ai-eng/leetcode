class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        special = []
        for i in range(n):
            if n % (i + 1) == 0:
                special.append(nums[i])
        sum = 0
        for i in range(len(special)):
            sum += special[i]*special[i]
        return sum
        