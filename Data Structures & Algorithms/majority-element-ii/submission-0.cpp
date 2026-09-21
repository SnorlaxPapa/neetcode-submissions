class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        /*
        max two elements can appear more than n/3 times
        the first scan is to find the two candidates
        the second is to verify if they are majority candidates
        */
        int num1, num2;
        int cnt1 = 0;
        int cnt2 = 0;

        for (size_t i = 0; i < nums.size(); ++i){
            if (nums[i] == num1) ++cnt1;
            else if (nums[i] == num2) ++cnt2;
            else if (cnt1 == 0){
                num1 = nums[i];
                cnt1 = 1;
            }
            else if (cnt2 == 0){
                num2 = nums[i];
                cnt2 = 1;
            }
            else{
                --cnt1;
                --cnt2;
            }
        }

        cnt1 = 0;
        cnt2 = 0;

        for (int num : nums){
            if (num == num1) cnt1++;
            else if (num == num2) cnt2++;
        }

        vector<int> res;
        int n = nums.size();
        if (cnt1 > n/3) res.push_back(num1);
        if (cnt2 > n/3) res.push_back(num2);

        return res;
    }
};