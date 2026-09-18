class MyHashMap {
private:
    struct ListNode {
        int key;
        int value;
        ListNode* next;
        ListNode(int key, int value)
            : key(key),
              value(value), 
              next(nullptr){}
    };
    
    int hash(int key){
        return key % 10000;
    }

    std::vector<ListNode*> set;

public:
    MyHashMap() {
        set.resize(10000);
        for (auto& bucket: set){
            bucket = new ListNode(-1, -1);
        }
    }
    
    void put(int key, int value) {
        ListNode* cur = set[hash(key)];
        while (cur->next){
            if (cur->next->key == key){
                cur->next->value = value;
                return;
            }
            cur = cur->next;
        }
        cur->next = new ListNode(key, value);
        return;
    }
    
    int get(int key) {
        ListNode* cur = set[hash(key)];
        while (cur->next){
            if (cur->next->key == key) return cur->next->value;
            cur = cur->next;
        }
        return -1;
    }
    
    void remove(int key) {
        ListNode* cur = set[hash(key)];
        while (cur->next){
            if (cur->next->key==key){
                ListNode* tmp = cur->next;
                cur->next = cur->next->next;
                delete tmp;
                return;
            }
            cur = cur->next;
        }
    }
};

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap* obj = new MyHashMap();
 * obj->put(key,value);
 * int param_2 = obj->get(key);
 * obj->remove(key);
 */