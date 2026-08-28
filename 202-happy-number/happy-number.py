class Solution:
    def happy(self, n):
        s = 0
        while n > 0:
            digit = n % 10
            s += digit * digit
            n //= 10
        return s

    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1 and n not in seen:
            seen.add(n)
            n = self.happy(n)

        return n == 1