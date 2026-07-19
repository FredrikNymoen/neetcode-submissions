class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count={}

        for string in s:
            count[string] = count.get(string,0) + 1
        
        for string in t:
            if string not in count or count[string]==0:
                return False
            count[string] -= 1
        
        return True