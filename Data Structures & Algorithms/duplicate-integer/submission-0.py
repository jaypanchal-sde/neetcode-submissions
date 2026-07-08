class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        appears_list = []
        for i in nums:
            if i not in appears_list:
                appears_list.append(i)
            else:
                return True
        return False