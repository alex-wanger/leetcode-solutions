/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    ArrayList<ListNode> list = new ArrayList<>();
    public boolean hasCycle(ListNode head) {
        if (head == null) {
            return false;
        }

        while (head.next != null) {
            for (int i = 0; i < list.size(); i++) {
                if (head == list.get(i)) {
                    return true;
                }
            }
            list.add(head);
            head = head.next;
        }
        return false;
    }
}
