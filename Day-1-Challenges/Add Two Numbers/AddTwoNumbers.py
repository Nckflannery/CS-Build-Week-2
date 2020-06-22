## Bad brute force attempt
# class Solution:
#     def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
#         stack = []
#         while l1:
#             stack.append(l1.val)
#             l1 = l1.next
#         stack1 = []
#         while l2:
#             stack1.append(l2.val)
#             l2 = l2.next

#         rstack = [] 
#         while stack:
#             rstack.append(stack.pop())

#         rstack1 = []
#         while stack1:
#             rstack1.append(stack1.pop())

#         number = 0
#         for i, j in enumerate(rstack):
#             number += j * 10**i

#         number1 = 0
#         for i, j in enumerate(rstack1):
#             number1 += j * 10**i

#         out_num = number + number1
#         new_list = [ListNode(int(i)) for i in str(out_num)]

#         cur = -1
#         for i in new_list:
#             if cur == -1:
#                 i.next = None
#             else:
#                 i.next = new_list[cur]
#             cur += 1

#         new_list.reverse()
#         return new_list[0]

# # Second attempt...working solution
# class Solution:
#     def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
#         def str_to_int(ln: ListNode) -> int:
#             '''
#             Takes in listnode and returns it reversed as type int
#             '''
#             out = ''
#             while ln:
#                 out += str(ln.val)
#                 ln = ln.next
#             return int(out[::-1])
        
#         def int_to_ln(num: int) -> ListNode:
#             '''
#             Takes in integer, reverses it and converts to ListNode
#             '''
#             new = str(num)[::-1]
#             head = None
#             prev = None
#             for char in new:
#                 node = ListNode(int(char))
#                 if prev:
#                     prev.next = node
#                 prev = node
#                 if head is None:
#                     head = prev
#             return head
        
#         # Get int of each ListNode
#         int1 = str_to_int(l1)
#         int2 = str_to_int(l2)
#         # Get sum of ints and convert back to ListNode to return
#         return int_to_ln(int1 + int2)

# Third attemnpt (slight rework of attempt 2)
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        def ln_to_int(li: ListNode) -> int:
            num = 0
            mul = 1
            while li:
                num += li.val * mul
                mul *= 10
                li = li.next
            return num
        
        def sum_to_ln(num1: int, num2: int) -> ListNode:
            total = num1 + num2
            reverse = str(total)[::-1]
            prev = None
            head = None
            for i in reverse:
                node = ListNode(int(i))
                if prev:
                    prev.next = node
                prev = node
                if head is None:
                    head = prev
            return head
        
        num1 = ln_to_int(l1)
        num2 = ln_to_int(l2)
        return sum_to_ln(num1, num2)