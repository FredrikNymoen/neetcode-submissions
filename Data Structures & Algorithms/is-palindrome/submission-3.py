class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = "".join(c.lower() for c in s if c.isalnum())
        return newStr == newStr[::-1]