#include<algorithm>
class Solution {
private:
    std::vector<int> merge(const std::vector<int>& v1, const std::vector<int>& v2){
        std::vector<int> res {};
        res.reserve(v1.size() + v2.size());

        size_t i = 0;
        size_t j = 0;

        while (i < v1.size() && j < v2.size()){
            if (v1[i] <= v2[j]){
                res.push_back(v1[i]);
                ++i;
            }
            else{
                res.push_back(v2[j]);
                ++j;
            }
        }

        while (i < v1.size()){
            res.push_back(v1[i]);
            ++i;
        }
    
        while (j < v2.size()){
            res.push_back(v2[j]);
            ++j;
        }

        return res;
    } 

    std::vector<int> mergeSort(int left, int right, std::vector<int>& nums){
        if (left == right) return {nums[left]};

        int middle = left + (right - left)/2;
        int left2 = middle + 1;
        std::vector<int> v1 = mergeSort(left, middle, nums);
        std::vector<int> v2 = mergeSort(left2, right, nums);

        return merge(v1, v2);

    }

public:
    std::vector<int> sortArray(std::vector<int>& nums) {
        int left = 0;
        int right = nums.size() - 1;
        return mergeSort(left, right, nums);
    }
};