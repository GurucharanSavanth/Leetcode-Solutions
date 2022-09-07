# Runtime: 42 ms (Top 62.11%) | Memory: 13.9 MB (Top 56.09%)
class Solution:
    def fillCups(self, amount: List[int]) -> int:

        count = 0
        amount = sorted(amount, reverse=True)
        while amount[0] > 0:
            amount[0] -= 1
            amount[1] -= 1
            count += 1
            amount = sorted(amount, reverse=True)
        return count