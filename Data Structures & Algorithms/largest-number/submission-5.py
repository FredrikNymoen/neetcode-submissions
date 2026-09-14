from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        arr = [str(num) for num in nums]

        def compare(a,b):
            if a + b > b + a:
                return -1
            else:
                return 1

        arr.sort(key=cmp_to_key(compare))

        return str(int("".join(arr)))