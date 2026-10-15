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
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        ListNode *curr = head;
        ListNode *tmp_next = nullptr;
        ListNode *prevSegment = head;

        int i = 1;

        while (i < left){
            prevSegment = curr;
            curr = curr -> next;
            ++i;
        }

        ListNode *startNode = curr;
        ListNode *tmpNxt = nullptr;
        ListNode *prev = nullptr;

        int j = left;

        while (j <= right){
            tmpNxt = curr -> next;
            if (prev){
                curr -> next = prev;
            }
            prev = curr;
            curr = tmpNxt;
            j += 1;
        }

        if (left > 1){
            prevSegment -> next = prev;
        }
        else{
            head = prev;
        }
        startNode -> next = tmpNxt;

        return head;
    }
};