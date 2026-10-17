class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)

        def digit_sum(x):
            return sum(int(d) for d in str(x))

        arr = sorted(nums, key=lambda x: (digit_sum(x), x))

        pos = {val: i for i, val in enumerate(nums)}
        visited = [False] * n
        swaps = 0

        for i in range(n):
            if visited[i] or pos[arr[i]] == i:
                visited[i] = True
                continue

            cycle_size = 0
            j = i

            while not visited[j]:
                visited[j] = True
                j = pos[arr[j]]
                cycle_size += 1

            swaps += cycle_size - 1

        return swaps