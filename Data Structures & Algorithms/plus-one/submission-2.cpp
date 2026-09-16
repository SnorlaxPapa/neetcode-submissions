class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int carry = 1;
        int newSum;
        for (size_t i = digits.size(); i-- > 0;){
            newSum = digits[i] + carry;
            digits[i] = newSum % 10;
            carry = newSum / 10;
            
            if (carry == 0) break;
        }
        if (carry == 1){
            digits.insert(digits.begin(), 1);
        }

        return digits;
    }
};
