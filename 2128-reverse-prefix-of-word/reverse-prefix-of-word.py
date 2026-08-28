class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        w=len(word)
        for i in range (len(word)):
            if word[i]==ch:
                first=word[:i+1]
                second=word[i+1:]
                return first[::-1]+second
        return word        
        