class Solution:
    def fillCups(self, amount: List[int]) -> int:

        total = sum(amount)
        maximum = max(amount)

        return max(maximum, (total + 1) // 2)
        