class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int insert = 1;
        int prev = nums[0];
        int n = static_cast<int> (nums.size()); 

        for (int i = 1; i < n; ++i){
            if (nums[i] != prev){
                nums[insert] = nums[i];
                prev = nums[i];
                ++insert;
            }
        }

        return insert;
    }
};