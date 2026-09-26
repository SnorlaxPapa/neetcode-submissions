#include <algorithm>

class Solution {
public:
    int numRescueBoats(vector<int>& people, int limit) {
        std::sort(people.begin(), people.end());
        std::size_t left = 0, right = people.size() - 1;

        int boats = 0;
        while (left <= right){
            if (left == right){
                boats += 1;
                break;
            }

            if (people[left] + people[right] <= limit){
                ++left;
                --right;
            }
            else{
                --right;
            }

            boats += 1;
        }

        return boats;
    }
};