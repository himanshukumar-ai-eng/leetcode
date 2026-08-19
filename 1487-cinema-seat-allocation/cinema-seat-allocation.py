class Solution:
    def maxNumberOfFamilies(self, n, reservedSeats):
        rows = {}

        for row, seat in reservedSeats:
            rows[row] = rows.get(row, 0) | (1 << seat)

        ans = 2 * n

        for mask in rows.values():

            # 2,3,4,5
            left = (mask & 0b000000111100) == 0

            # 4,5,6,7
            middle = (mask & 0b0011110000) == 0

            # 6,7,8,9
            right = (mask & 0b1111000000) == 0

            if left and right:
                continue

            elif left or middle or right:
                ans -= 1

            else:
                ans -= 2

        return ans