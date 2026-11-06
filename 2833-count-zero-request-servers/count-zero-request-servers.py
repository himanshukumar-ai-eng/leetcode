from typing import List

class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:

        logs.sort(key=lambda a: a[1])

        q = sorted((t, i) for i, t in enumerate(queries))

        ans = [0] * len(queries)
        freq = {}
        left = right = active = 0

        for t, idx in q:
            start = t - x

            while right < len(logs) and logs[right][1] <= t:
                s = logs[right][0]
                freq[s] = freq.get(s, 0) + 1
                if freq[s] == 1:
                    active += 1
                right += 1

            while left < right and logs[left][1] < start:
                s = logs[left][0]
                freq[s] -= 1
                if freq[s] == 0:
                    active -= 1
                    del freq[s]
                left += 1

            ans[idx] = n - active

        return ans