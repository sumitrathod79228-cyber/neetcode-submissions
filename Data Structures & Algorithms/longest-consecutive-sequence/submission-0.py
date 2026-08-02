class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mape=set(nums)
        logest=0
        for num in nums:
            if num-1 not in mape:
                length=1
                while num+length in mape :
                    length+=1
                logest=max(logest,length)
        return logest            
            