class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > num * 9:
            return ""
        a = ["9"] * (sum // 9)
        r = sum % 9
        if r:
            a.append(str(r))
        a.extend(["0"] * (num - len(a)))
        return "".join(a)