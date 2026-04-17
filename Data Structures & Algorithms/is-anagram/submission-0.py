class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = {}
        
        for n in s:
            counts[n] = counts.get(n, 0) + 1
        
        for n in t:
            counts[n] = counts.get(n, 0) - 1
        
        for val in counts.values():
            if val != 0:
                return False
        
        return True