# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
# 
# Merge all the linked-lists into one sorted linked-list and return it.
# 
# 
# 
# Example 1:
# 
# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6

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
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        res = None

        def merge(t,s):
            ret = t if t.val<s.val else s
            last = None
            while t and s:
                if t.val<s.val:
                    if not last:
                        last = t
                    else:
                        last.next = t
                        last = last.next
                    t = t.next
                else:
                    if not last:
                        last = s
                    else:
                        last.next = s
                        last = last.next
                    s = s.next
                last.print_list()
            if s and last:
                last.next = s
            if t and last:
                last.next = t
            return ret
        for l in lists:
            if not res:
                res = l
            else:
                res = merge(res, l)
        return res

# Given the head of a linked list, remove the nth node from the end of the list and return its head.

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if n == 0 or (not head):
            return head
        l = 1
        prev = node = head
        while node:
            if l== n:
                if not node.next:
                    return head.next
            elif l > n:
                if not node.next:
                    prev.next = prev.next.next
                    return head
                else:
                    prev = prev.next
            node = node.next
            l += 1

        if l < n:
            return head


if __name__ == "__main__":
    l1 = ListNode()
    l1.assign([2,3,3,6])
    l2 = ListNode()
    l2.assign([5,6,8])
    l3 = ListNode()
    l3.assign([1,1,2,9])
    s = Solution()
    l4 = [l1, l2, l3]
    print("Expected output: [1, 1, 2, 2, 3, 3, 5, 6, 6, 8, 9]")
    print("Actual output: ", end="")
    s.mergeKLists(l4).print_list()

    head = ListNode()
    head.assign([1,2])
    n = 1
    print("Expected output: [1]")
    s.removeNthFromEnd(head, n).print_list()
