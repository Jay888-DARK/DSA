class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        frequency={}
        l=0
        max_len=0
        for i in range(len(nums)):
            cur_val = nums[i]

            frequency[cur_val]=frequency.get(cur_val,0)+1

            while frequency[cur_val]>k:
                left_v=nums[l]
                frequency[left_v]-=1
                l+=1
            max_len=max(max_len,i-l+1)
        return max_len        


    

        
               



        