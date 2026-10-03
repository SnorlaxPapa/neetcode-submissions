#include <unordered_map> 
#include <algorithm>

class FreqStack {
private:
    std::unordered_map<int, int> valFreq;
    std::unordered_map<int, std::vector<int>> freqValMap;
    int maxCount = 0;
public:
    FreqStack() {
        
    }
    
    void push(int val) {
        valFreq[val] += 1;
        int freq = valFreq[val];
        maxCount = std::max(freq, maxCount);
        freqValMap[freq].push_back(val);
    }
    
    int pop() {
        int value = freqValMap[maxCount].back();
        freqValMap[maxCount].pop_back();
        valFreq[value] -= 1;
        
        if (freqValMap[maxCount].empty()){
            --maxCount;
        }

        return value;
    }
};

/**
 * Your FreqStack object will be instantiated and called as such:
 * FreqStack* obj = new FreqStack();
 * obj->push(val);
 * int param_2 = obj->pop();
 */