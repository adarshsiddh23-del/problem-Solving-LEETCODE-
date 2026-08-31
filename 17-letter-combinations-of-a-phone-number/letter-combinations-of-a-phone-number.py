class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        ans = []

        def backtrack(i, current):
            if i == len(digits):
                ans.append(current)
                return

            for ch in phone[digits[i]]:
                backtrack(i + 1, current + ch)

        backtrack(0, "")

        return ans        
