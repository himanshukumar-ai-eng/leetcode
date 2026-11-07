from typing import List
import heapq

class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        free = [(w, i) for i, w in enumerate(servers)]
        heapq.heapify(free)

        busy = []
        ans = []

        for j, task in enumerate(tasks):
            time = max(time, j) if j > 0 else 0

            while busy and busy[0][0] <= time:
                t, w, i = heapq.heappop(busy)
                heapq.heappush(free, (w, i))

            if not free:
                time = busy[0][0]

                while busy and busy[0][0] <= time:
                    t, w, i = heapq.heappop(busy)
                    heapq.heappush(free, (w, i))

            w, i = heapq.heappop(free)
            ans.append(i)

            heapq.heappush(busy, (time + task, w, i))

        return ans