class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        rightmax=0
        leftmax=0
        l=0
        r=n-1
        ans=0
        while l<r:
            leftmax=max(leftmax,height[l])
            rightmax=max(rightmax,height[r])
            if leftmax<rightmax:
                ans+=leftmax-height[l]
                l+=1
            else :
                ans+=rightmax-height[r]
                r-=1
        return ans            
        