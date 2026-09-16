#include <functional>
#include <unordered_set>

class Solution {
public:
    bool isHappy(int n) {
        std::unordered_set<int> seen;
        return checkCyclical(seen, n);
    }

    int computeSquare(int n){
        int remainder;
        int squared = 0;
        while (n){
            remainder = n % 10;
            n /= 10;
            squared += remainder * remainder;
        }
        return squared;
    }

    bool checkCyclical(
        std::unordered_set<int>& seen,
        int& number
    ){
        if (number == 1){
            return true;
        }
        if (seen.find(number) != seen.end()){
            return false;
        }

        seen.insert(number);

        int squared = computeSquare(number);
        return checkCyclical(seen, squared);
    }
};
