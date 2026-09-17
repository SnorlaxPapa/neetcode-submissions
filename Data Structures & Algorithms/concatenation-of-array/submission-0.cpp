class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        std::vector<int> ans;
        std::size_t n = nums.size();
        for (std::size_t i = 0; i < n * 2; ++i){
            ans.push_back(nums[i % n]);
        }
        return ans;
    }
};