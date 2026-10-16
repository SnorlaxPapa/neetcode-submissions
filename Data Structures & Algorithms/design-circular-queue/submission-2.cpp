struct ListNode{
    int val;
    ListNode* next;

    ListNode(int val, ListNode* next): val(val), next(next){}
};

class MyCircularQueue {
    //maintain head tail 
private:
    ListNode* head;
    ListNode* tail;
    int size = 0;
    int limit;

public:
    MyCircularQueue(int k): limit(k){
        head = new ListNode(-1, nullptr);
        tail = head;
        ListNode* curr = head;

        for (int i = 1; i < k; ++i){
            ListNode* newNode = new ListNode(-1, nullptr);
            curr -> next = newNode;
            curr = curr -> next;
            tail = curr;
        }
        tail -> next = head;
    }
    
    bool enQueue(int value) {
        if (size == limit) return false;

        size += 1;
        if (head -> val == -1){
            head -> val = value;
            tail = head;
            return true;
        }

        tail = tail -> next;
        tail -> val = value;

        return true;
    }
    
    bool deQueue() {
        if (size == 0) return false;

        size -= 1;
        head = head -> next;
        if (size == 0) head -> val = -1;
        return true;
    }
    
    int Front() {
        return head -> val;
    }
    
    int Rear() {
        return tail -> val;
    }
    
    bool isEmpty() {
        return size == 0;
    }
    
    bool isFull() {
        return size == limit; 
    }
};

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * MyCircularQueue* obj = new MyCircularQueue(k);
 * bool param_1 = obj->enQueue(value);
 * bool param_2 = obj->deQueue();
 * int param_3 = obj->Front();
 * int param_4 = obj->Rear();
 * bool param_5 = obj->isEmpty();
 * bool param_6 = obj->isFull();
 */