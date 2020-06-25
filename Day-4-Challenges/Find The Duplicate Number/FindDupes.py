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

        # Slightly better solution (no list)
        lookup = {}
        for i in nums:
          if i in lookup:
            lookup[i] = 1
          else:
            lookup[i] = 0
          if lookup[i] == 1:
            return i