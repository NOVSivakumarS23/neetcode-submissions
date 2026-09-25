/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    bool hasCycle(ListNode* head) {
        if(head==nullptr){return false;}
        ListNode* fast = head->next;
        if(fast==nullptr){return false;}
        ListNode* slow = head;
        while(true){
            if(fast==slow){return true;}
            fast = fast->next;
            if(fast==nullptr){return false;}
            if(fast==slow){return true;}
            fast = fast->next;
            if(fast==nullptr){return false;}
            slow = slow->next;
        }
    }
};
