class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref_prod = [1] * len(nums)
        for i in range(1, len(nums)):
            pref_prod[i] = pref_prod[i-1] * nums[i-1]
        
        suff_prod = [1] * len(nums)
        for j in range(len(nums) - 2, -1, -1):
            suff_prod[j] = suff_prod[j+1] * nums[j+1]
        
        ans = [0] * len(nums)

        for k in range(len(nums)):
            ans[k] = pref_prod[k] * suff_prod[k]
        
        return ans