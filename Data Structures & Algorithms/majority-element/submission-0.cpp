class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int candidate = 0;
        int count = 0;

        for (const auto &val: nums){
            if (count == 0) candidate = val;
            if (candidate != val) --count;
            else ++count;
        }

        return candidate;
    }
};