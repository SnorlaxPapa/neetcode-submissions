#include <algorithm>

class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        std::sort(nums.begin(), nums.end());
        int n = static_cast<int> (nums.size()); 
        int left2, right2, sum;
        std::vector<std::vector<int>> res;

        for (int left1 = 0; left1 < n - 3; ++left1) {
            if (left1 > 0 && nums[left1] == nums[left1 - 1]) {
                continue;
            }

            for (int right1 = left1 + 1; right1 < n - 2; ++right1) {
                if (right1 > left1 + 1 &&
                    nums[right1] == nums[right1 - 1]) {
                    continue;
                }

                int left2 = right1 + 1;
                int right2 = n - 1;

                while (left2 < right2) {
                    long long sum =
                        static_cast<long long>(nums[left1])
                        + nums[right1]
                        + nums[left2]
                        + nums[right2];

                    if (sum < target) {
                        ++left2;
                    }
                    else if (sum > target) {
                        --right2;
                    }
                    else {
                        res.push_back({
                            nums[left1],
                            nums[right1],
                            nums[left2],
                            nums[right2]
                        });

                        ++left2;
                        --right2;

                        while (left2 < right2 &&
                            nums[left2] == nums[left2 - 1]) {
                            ++left2;
                        }

                        while (left2 < right2 &&
                            nums[right2] == nums[right2 + 1]) {
                            --right2;
                        }
                    }
                }
            }
        }
        
        return res;
    }
};