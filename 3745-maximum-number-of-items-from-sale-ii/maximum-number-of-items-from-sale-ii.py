
class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        items.sort(key=lambda x: x[1])

        n = len(items)
        mx = max(factor for factor, price in items)

        freq = [0] * (mx + 1)

        for factor, price in items:
            freq[factor] += 1

        # Count how many item types each factor can unlock
        for i in range(1, mx + 1):
            for j in range(i * 2, mx + 1, i):
                freq[i] += freq[j]

        min_price = items[0][1]
        ans = 0

        # Take the profitable copies first
        for factor, price in items:

            if price > 2 * min_price:
                break

            gain = freq[factor] - 1

            if gain <= 0:
                continue

            take = min(gain, budget // price)

            ans += take * 2
            budget -= take * price

        # Spend remaining budget on cheapest items
        ans += budget // min_price

        return ans
