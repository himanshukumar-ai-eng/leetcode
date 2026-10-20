from typing import List

class Solution:
    def sortableIntegers(self, nums: List[int]) -> int:
        n = len(nums)
        target = sorted(nums)
        ans = 0

        def is_rotation(a, b):
            k = len(a)
            lps = [0] * k
            j = 0

            for i in range(1, k):
                while j and a[i] != a[j]:
                    j = lps[j - 1]
                if a[i] == a[j]:
                    j += 1
                    lps[i] = j

            j = 0
            for i in range(2 * k - 1):
                x = b[i % k]

                while j and x != a[j]:
                    j = lps[j - 1]

                if x == a[j]:
                    j += 1

                if j == k:
                    return True

            return False

        for k in range(1, n + 1):
            if n % k:
                continue

            valid = True

            for i in range(0, n, k):
                if not is_rotation(nums[i:i + k], target[i:i + k]):
                    valid = False
                    break

            if valid:
                ans += k

        return ans