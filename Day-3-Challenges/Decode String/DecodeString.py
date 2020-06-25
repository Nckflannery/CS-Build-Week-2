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


    ## Solution: Thanks to Michelle Sirimanivong
        stack = []
        
        # loop through string
        for i in range(len(s)):
            
            # append characters that are not []
            # if ], loop through characters in brackets to add to decoded
            if s[i] == ']':
                
                # create variable to store decoded characters
                decoded = ''
                
                # loop through stack if it's not [
                while stack[-1] != '[':
                    
                    # pop last char from stack and add to decoded
                    decoded = stack.pop() + decoded
                    
                # pop last char in stack, which should be [
                stack.pop()
                
                # find k
                k = ''
                # while there is a stack and the last item of the stack is a number
                while stack and stack[-1].isdigit():
                    # add that to k
                    k = stack.pop() + k
                
                # multiply k with decoded & add to stack
                decoded = int(k) * decoded
                stack.append(decoded)
                
            # add all characters into stack
            else:
                stack.append(s[i])
                
        # join decoded to make new string
        return ''.join(stack)