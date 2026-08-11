class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        a=len(nums)
        b=nums[0]
        for i in range(1,a):
           
            if nums[i] == nums[i-1]+1:
               
                b+=nums[i]
            else:
                
                break

        while b in nums :
            b+=1
            
        return b               



        