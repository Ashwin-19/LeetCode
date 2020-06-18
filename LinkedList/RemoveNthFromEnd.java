/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        
        ListNode ptr = head;
        int size = 0;
        
        while(ptr!=null){ size++; ptr=ptr.next; }
        
        int pos = size-n;
        
        if(pos==0)
            head = head.next;
        else
        {
            ptr = head;
            
            while(pos-->1)
            {
                ptr = ptr.next;
            }
            
            ptr.next = ptr.next.next;
        }
        
        return head;
    }
}