from typing import List

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        size = 4 * n

        s1 = [0] * size
        s2 = [0] * size
        lazy = [0] * size

        def apply(node, l, r, val):
            length = r - l + 1
            s2[node] = (s2[node] + 2 * val * s1[node] + length * val * val) % MOD
            s1[node] = (s1[node] + length * val) % MOD
            lazy[node] += val

        def push(node, l, r):
            if lazy[node] and l != r:
                mid = (l + r) // 2
                apply(node * 2, l, mid, lazy[node])
                apply(node * 2 + 1, mid + 1, r, lazy[node])
                lazy[node] = 0

        def update(node, l, r, ql, qr, val):
            if ql <= l and r <= qr:
                apply(node, l, r, val)
                return

            push(node, l, r)
            mid = (l + r) // 2

            if ql <= mid:
                update(node * 2, l, mid, ql, qr, val)
            if qr > mid:
                update(node * 2 + 1, mid + 1, r, ql, qr, val)

            s1[node] = (s1[node * 2] + s1[node * 2 + 1]) % MOD
            s2[node] = (s2[node * 2] + s2[node * 2 + 1]) % MOD

        last = {}
        ans = 0

        for i, x in enumerate(nums):
            prev = last.get(x, -1)

            # Increase distinct counts for affected subarrays
            update(1, 0, n - 1, prev + 1, i, 1)
            last[x] = i

            ans = (ans + s2[1]) % MOD

        return ans