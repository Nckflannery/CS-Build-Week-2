# # Naive first attempt, brute force nested for loops
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for j in range(len(nums)):
#                 if nums[i] + nums[j] == target and i != j:
#                     return [i, j]

# Working solution with lookup table to decrease time complexity from O(n^2) to O(n)
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    lookup = {}
    for i, j in enumerate(nums):
      comp = target - j
      if comp in lookup:
        return [lookup[comp], i]
      else:
        lookup[j] = i