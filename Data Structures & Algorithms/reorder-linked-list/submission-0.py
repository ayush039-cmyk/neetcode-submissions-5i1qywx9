class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Collect all nodes (not values)
        nodes = []
        temp = head
        while temp:
            nodes.append(temp)
            temp = temp.next

        l, r = 0, len(nodes) - 1
        while l < r:
            nodes[l].next = nodes[r]
            l += 1
            if l == r:
                break
            nodes[r].next = nodes[l]
            r -= 1

        nodes[l].next = None  # terminate the list