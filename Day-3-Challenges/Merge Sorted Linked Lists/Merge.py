# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
First Solution
Runtime: 44 ms, faster than 24.68% of Python3 online submissions for Merge Two Sorted Lists.
Memory Usage: 13.8 MB, less than 79.69% of Python3 online submissions for Merge Two Sorted Lists.
'''
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
      # Check for empty lists, if so return only other list
      if l1 == []:
        return l2
      if l2 == []:
        return l1
      # Create new list to hold sorted elements of both lists
      arr = []
      # While there are elements in l1 and l2
      while l1 and l2:
        if l1.val <= l2.val:
          arr.append(l1.val)
          l1 = l1.next
        elif l2.val < l1.val:
          arr.append(l2.val)
          l2 = l2.next
      # Catch when one list runs out of elements before other
      while l1 or l2:
        if l1:
          arr.append(l1.val)
          l1 = l1.next
        if l2:
          arr.append(l2.val)
          l2 = l2.next
      
      # Convert arr (list) to ListNode
      node = None
      prev = None
      new_node = None
      for i in range(len(arr), 0, -1):
        # Create ListNodes starting with the last
        new_node = ListNode(arr[i-1])
        if node == None:
          node = ListNode(arr[i-1], None)
          prev = node
        else:
          new_node.next = prev
          prev = new_node
      return new_node