
# Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

# You may not alter the values in the list's nodes, only nodes themselves may be changed.
# Input: head = [1,2,3,4,5], k = 2
# Output: [2,1,4,3,5]


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

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        stack = []
        l = 0
        res = None
        last = None
        node =head
        while l<k and node:
            stack.append(node)
            node = node.next
            l += 1
            if l==k:
                nh = stack.pop()
                if not res:
                    res = nh
                else:
                    last.next = nh
                while stack:
                    n = stack.pop()
                    nh.next = n
                    nh = n
                last = nh
                nh.next = node
                l=0
        return res

if __name__ == "__main__":
    head = ListNode()
    head.assign([1,2,3,4,5])
    k = 3
    r = s.reverseKGroup(head, k)
    print("Expected Output: [3, 2, 1, 4, 5]")
    print("Actual Output: ", end ="")
    if r:
        r.print_list()
