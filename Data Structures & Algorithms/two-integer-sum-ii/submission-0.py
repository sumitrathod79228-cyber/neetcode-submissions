class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        freq={}
        for i in range(len(numbers)):
            need=target-numbers[i]
            if need in freq:
                return [freq[need],i+1]
            freq[numbers[i]]=i+1    