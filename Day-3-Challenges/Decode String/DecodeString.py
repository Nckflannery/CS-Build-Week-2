class Solution:
    def decodeString(self, s: str) -> str:
        # # First attempt, fails some tests
        # first = s.split('[')
        # second = []
        # nums = []
        # chars = []
        # for i in first:
        #     second+=(i.split(']'))
        # for i in second:
        #     if i.isdigit():
        #     nums.append(i)
        #     if i.isalpha():
        #     chars.append(i)
        # out = ''
        # for i, j in zip(nums, chars):
        #     out += (int(i) * j)
        # return out 

    # # I think we need a recursive solution
    # # Attempt 2 Still not working :(
    #   nums = {}
    #   chars = {}
    #   out_string = ''
      
    #   self.recurser(s, nums, chars)
      
    #   for i, j in zip(nums.values(), chars.values()):
    #     out_string += int(i) * j
    #   return out_string
    
    # def recurser(self, li: list, nums: dict, chars: dict):
    #   for i, j in enumerate(li):
    #     if isinstance(li, list):
    #       recurser(j, nums, chars)
    #     else:
    #       if j.isdigit():
    #         nums[i] = j
    #       if j.isalpha():
    #         chars[i] = j