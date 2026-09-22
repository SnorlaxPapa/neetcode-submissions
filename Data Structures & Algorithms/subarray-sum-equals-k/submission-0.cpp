#include <unordered_map>

class Solution {
public:
    int subarraySum(std::vector<int>& nums, int k) {
        /*
        Finds num subarrays with sum = k
        brute force is O(n)^2 to explore all subarrays in nums
        
        prefixSum[i] = sum nums[:i+1]
        iterate through the array again

        so for [2, -1, 1, 2] -> [2, 1, 2, 4]

        we can get sum of subarray nums[i:j + 1] by prefixSum[j] - prefixSum[i],
        and we want this to be == k. 
        that is, prefixSum[i] = prefixSum[j] - k

        we can maintain an unordered_map with mapping sum: count. then, we can simply look up the counts of prefixSum[i] with sum == prefixSum[j] - k
        */
        std::unordered_map<int, int> count;
        count[0] = 1;

        int prev = 0, subarrays = 0;
        int sum;

        for (const int& num: nums){
            cout << num << endl;
            sum = prev + num;

            if (count.contains(sum - k)){
                subarrays += count[sum - k];
            }

            count[sum]++;
            prev = sum;
        }
        return subarrays;
    }
};