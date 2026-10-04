class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        std::size_t left = 0;
        std::size_t right = nums.size();
        std::size_t mid;

        while (left < right){
            mid = left + (right - left) / 2;
            
            if (nums[mid] == target){
                return mid;
            }
            
            if (nums[mid] > target){
                right = mid;
            }

            else{
                left = mid + 1;
            }
        }
        return static_cast<int> (left);
    }
};