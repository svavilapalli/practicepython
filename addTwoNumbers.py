# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Example:
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

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
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        node1 = l1
        node2 = l2
        l3= ListNode()
        res = l3
        while node1 != None and node2!=None:
            res.val = (node1.val + node2.val + carry) % 10
            carry = (node1.val + node2.val + carry)//10
            node1 = node1.next
            node2 = node2.next
            if carry>0 or node1 or node2:
                res.next = ListNode()
            res = res.next
        if node1 == None:
            node1 = node2
        while node1 != None:
            res.val = (node1.val + carry) % 10
            carry = (node1.val + carry)//10
            node1 = node1.next
            if carry> 0 or node1:
                res.next = ListNode()
            res = res.next
        if carry>0:
            res.val = carry
        return l3



if __name__ == "__main__":
    l1 = ListNode()
    l1.assign([2,4,3])
    l2 = ListNode()
    l2.assign([5,6,4])
    s = Solution()
    print("Expected output : [7, 0, 8]")
    print("Actual output : ", end="")
    s.addTwoNumbers(l1, l2).print_list()
