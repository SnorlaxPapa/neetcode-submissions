#include <utility>

class Solution {
public:
    void merge(std::vector<int>& nums1, int m, std::vector<int>& nums2, int n) {
        int i = m - 1;
        std::size_t insert = nums1.size() - 1;
        int j = n - 1;

        while(j >= 0){
            if (i < 0 || nums2[j] >= nums1[i]){
                nums1[insert] = nums2[j];
                --j;
            }
            else{
                std::swap(nums1[i], nums1[insert]);
                --i;
            }
            --insert;
        }        
    }
};