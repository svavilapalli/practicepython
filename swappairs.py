# Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

# Example 1:
# Input: head = [1,2,3,4]
# Output: [2,1,4,3]


from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next 
             
    def print_list(self):
        node = self
        l = []
        while node:
            l.append(node.val)
            node = node.next
        print(l)

    def assign(self, vals: List[int]):
        node = self
        for i in range(len(vals)-1):
            node.val = vals[i]
            node.next = ListNode()
            node = node.next
        node.val = vals[-1]


class Solution:
def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
            return head
        base = head.next
        first = head
        second = head.next
        last = None
        while first and second:
            if last:
                last.next = second
            third = second.next
            second.next = first
            first.next =third
            last = first
            first = third
            if first:
                second = first.next
        return base


s= Solution()
l = ListNode()
l.assign([1,2,3,4])
print("Expected Output: [2,1,4,3]")
print("Actual Output: ",end="")
s.swapPrairs(l).print_list()
