class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_number = 0
        current_number_count = 0
        for i in nums:
            if i == 1:
                current_number_count +=1
                if current_number_count > max_number:
                    max_number = current_number_count
            else:
                current_number_count = 0
        return max_number

        