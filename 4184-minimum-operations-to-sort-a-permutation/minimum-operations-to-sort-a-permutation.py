class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n = len(nums)

        if nums == list(range(n)):
            return 0

        # Check if nums is a rotation of sorted order
        if all(nums[(i + 1) % n] == (nums[i] + 1) % n
               for i in range(n)):
            k = nums[0]
            return min(n - k, k + 2)

        # Check if nums is a rotation of reversed sorted order
        if all(nums[(i + 1) % n] == (nums[i] - 1) % n
               for i in range(n)):
            k = (n - 1 - nums[0]) % n
            return min(k + 1, n - k + 1)

        return -1