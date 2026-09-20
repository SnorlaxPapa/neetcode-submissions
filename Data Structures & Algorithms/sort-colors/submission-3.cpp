class Solution {
public:
    void sortColors(vector<int>& nums) {
        int zeroPos = 0;
        int twoPos = nums.size() - 1;
        int i = 0;

        while(i <= twoPos){
            if (nums[i] == 0){
                nums[i] = nums[zeroPos];
                nums[zeroPos] = 0;
                ++zeroPos;
            }
            else if (nums[i] == 2){
                nums[i] = nums[twoPos];
                nums[twoPos] = 2;
                --twoPos;
                --i;
            }
            ++i;
        }
    }
};