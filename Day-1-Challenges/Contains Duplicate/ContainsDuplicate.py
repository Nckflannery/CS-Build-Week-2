class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        ## Naive first pass solution
        # counts = {}
        # out = False
        # for i in nums:
        #     if i in counts:
        #         counts[i] += 1
        #     else:
        #         counts[i] = 1
        # for i in nums:
        #     if counts[i] > 1:
        #         out = True
        # return out
        
        # Second attempt
        return False if len(set(nums)) == len(nums) else True