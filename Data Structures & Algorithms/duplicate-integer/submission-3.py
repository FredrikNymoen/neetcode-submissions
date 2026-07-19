class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        list = []

        for number in nums:
            print(number)
            if number in list: return True
            else: list.append(number)
        return False