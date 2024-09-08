from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        def get_length(node: Optional[ListNode]) -> int:
            length = 0
            while node:
                length += 1
                node = node.next
            return length

        length = get_length(head)
        base_size = length // k
        extra_parts = length % k

        parts = []
        current = head
        
        for i in range(k):
            part_head = current
            part_size = base_size + (1 if i < extra_parts else 0)
            
            for _ in range(part_size - 1):
                if current:
                    current = current.next
            
            if current:
                next_part = current.next
                current.next = None
                current = next_part
            
            parts.append(part_head)
        
        return parts
