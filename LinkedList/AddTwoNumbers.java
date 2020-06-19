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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        
        ListNode p1 = l1;
        ListNode p2 = l2;
        
        int c1 = 0;
        while(p1!=null)
        {
            p1 = p1.next;
            c1++;
        }
        
        int c2 = 0;
        while(p2!=null)
        {
            p2 = p2.next;
            c2++;
        }
        
        int diff = c1-c2;
        
        if(diff>=0){ p1 = l1; p2 = l2; }
        else{ p1 = l2; p2 = l1; }
        
        int sum = 0;
        int carry = 0;
        
        while(p1!=null)
        {
            if(p2!=null)
            {
                sum = p1.val+p2.val+carry;
                
                p1.val = sum%10;
                carry = (sum - sum%10)/10;
                
                p2 = p2.next;
            }
            else
            {
                sum = p1.val + carry;
                
                p1.val = sum%10;
                carry = (sum - sum%10)/10;
            }
            
            if(p1.next==null && carry != 0)
            {
                ListNode node = new ListNode(carry);
                p1.next = node;
                p1 = p1.next;
            }
            
            p1 = p1.next;
        }
        
        
        if(diff>=0){return l1;}
        else{return l2;}
    }
}