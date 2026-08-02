class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n=len(arr)
        max_val=-1
        ans=[-1]*(n)
        for i in range(len(arr)-1,-1,-1):
            ans[i]=max_val
            if arr[i] > max_val:
                max_val = arr[i]
        return ans