#include <vector>

class Solution {
private:
    void merge(std::vector<int>& nums, std::vector<int>& temp, int left, int mid, int right) {
        int i = left;
        int j = mid + 1;
        int k = left;

        // Merge two sorted halves into temp
        while (i <= mid && j <= right) {
            if (nums[i] <= nums[j]) {
                temp[k++] = nums[i++];
            } else {
                temp[k++] = nums[j++];
            }
        }

        while (i <= mid) temp[k++] = nums[i++];
        while (j <= right) temp[k++] = nums[j++];

        // Copy back to original array for this range
        for (int p = left; p <= right; ++p) {
            nums[p] = temp[p];
        }
    }

    void mergeSort(std::vector<int>& nums, std::vector<int>& temp, int left, int right) {
        if (left >= right) return;

        int mid = left + (right - left) / 2;
        mergeSort(nums, temp, left, mid);
        mergeSort(nums, temp, mid + 1, right);

        // Optimization: skip merge if already in sorted order
        if (nums[mid] <= nums[mid + 1]) return;

        merge(nums, temp, left, mid, right);
    }

public:
    std::vector<int> sortArray(std::vector<int>& nums) {
        std::vector<int> temp(nums.size());
        mergeSort(nums, temp, 0, nums.size() - 1);
        return nums;
    }
};