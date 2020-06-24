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