#include <utility>

class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        /*
        skip all negative integers
        when encounter positive integers
        O(1) space means no data structures

        modify in place

        */
        int n = static_cast<int>(nums.size());
        int temp;

        for (int i = 0; i < n; ++i){
            while (nums[i] >= 1 && nums[i] <= n && nums[nums[i] - 1] != nums[i]){
                std::swap(nums[i], nums[nums[i] - 1]);
            }
        }

        for (int i = 0; i < n; ++i){
            if (nums[i] != i + 1) return i + 1;
        }

        return n + 1;
    }
};