class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(1, head)

        current_sum = 1
        prefix_sum = {current_sum: [head]}
        temp = head.next
        while temp:
            current_sum += temp.val
            if current_sum in prefix_sum:
                for t in prefix_sum[current_sum]:
                    t.next = temp.next

            prefix_sum[current_sum] = prefix_sum.get(current_sum, [])
            prefix_sum[current_sum].append(temp)
            temp = temp.next

        return head.next
