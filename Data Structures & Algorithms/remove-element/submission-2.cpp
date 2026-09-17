class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int j = static_cast<int>(nums.size()) - 1;

        for (int i = 0; i <= j ; ++i){
            while (j >= i && nums[j] == val) --j; 
            if (j < i) break;
            if (nums[i] == val){
                int temp = nums[i];
                nums[i] = nums[j];
                nums[j] = temp;

                --j;
            }
        }

        return j + 1;
    }
};