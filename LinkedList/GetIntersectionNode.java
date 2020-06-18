/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {        
        
        int s1 = 0;
        ListNode p1 = headA;
        while(p1!=null)
        {
            p1 = p1.next;
            s1++;
        }
        
        
        int s2 = 0;
        ListNode p2 = headB;
        while(p2!=null)
        {
            p2 = p2.next;
            s2++;
        }
        
        int diff = s1-s2;
        
        if(diff<=0)
        {
            p2 = headA;
            p1 = headB;
        }
        else
        {
            p1 = headA;
            p2 = headB;
        }
        
        if(diff<0)
            diff = -diff;
        
        for(int i = 0; i < diff; i++)
            p1 = p1.next;
        
        while(p1 != null && p2 != null)
        {            
            if(p1==p2)
            {
                return p1;
            }
            p1 = p1.next;
            p2 = p2.next;
        }
        return null;
    }
}