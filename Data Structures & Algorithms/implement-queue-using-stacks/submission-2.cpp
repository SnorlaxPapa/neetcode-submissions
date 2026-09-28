#include <stack>
#include <iostream>

class MyQueue {
private:
    std::stack<int> s1;
    std::stack<int> s2;

public:
    MyQueue() {}
    
    void push(int x) {
        s1.push(x); //s1 maintains a proper stack, s2 maintains the queue
    }
    
    int pop() {
        //invert s1 into a queue

        if (!s2.empty()){
            int first = s2.top();
            s2.pop();
            return first;
        }

        while (!s1.empty()){
            s2.push(s1.top());
            s1.pop();
        }

        int first = s2.top();
        s2.pop();

        return first;
    }
    
    int peek() {
        if (!s2.empty()){
            return s2.top();
        }

        while (!s1.empty()){
            s2.push(s1.top());
            s1.pop();
        }

        int top = s2.top();

        return top;
    }
    
    bool empty() {
        return s1.empty() && s2.empty();
    }
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */