class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        freq = {}

        for num in arr:
            if num in freq:
                freq[num]+=1
            else :
                freq[num]=1
        return len(freq.values()) == len(set(freq.values()))
        