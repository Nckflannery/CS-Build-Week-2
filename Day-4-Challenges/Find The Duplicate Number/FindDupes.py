class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # # First solution
        # lookup = {}
        # for i in nums:
        #   if i in lookup:
        #     lookup[i].append(i)
        #   else:
        #     lookup[i] = [i]
        #   if len(lookup[i]) > 1:
        #     return i

        ## Not O(1) space complexity
        # lookup = {}
        # for i in nums:
        #   if i in lookup:
        #     lookup[i] = 1
        #   else:
        #     lookup[i] = 0
        #   if lookup[i] == 1:
        #     return i
        
        nums.sort()
        for i in range(1, len(nums)):
          if nums[i] == nums[i - 1]:
            return nums[i]