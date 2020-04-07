class Solution:
    def singleNumber(self, nums: List[int]) -> int:      
        res = nums[0]
        for i in range(1,len(nums)):
            # XOR of a number with itself gives 0
            # XOR of a number with 0 is the number itself
            res = res ^ nums[i] 
        return res
