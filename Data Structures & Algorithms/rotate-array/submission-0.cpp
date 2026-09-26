class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        int n = static_cast<int>(nums.size());
        k %= n;

        int moved = 0;

        for (int start = 0; moved < n; ++start) {
            int current = start;
            int previous = nums[start];

            do {
                int next = (current + k) % n;

                int temp = nums[next];
                nums[next] = previous;
                previous = temp;

                current = next;
                ++moved;
            }
            while (current != start);
        }
    }
};