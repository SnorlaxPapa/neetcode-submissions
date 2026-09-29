#include <cstdlib>

class Solution {
public:
    vector<int> asteroidCollision(vector<int>& asteroids) {
        std::vector<int> collisions;
        collisions.reserve(asteroids.size());

        for (size_t i = 0; i < asteroids.size(); ++i){
            //check if top is same dir. if same dir can just push in
            /* if different dir, while my stack is not empty
                same size, pop both, break. 
                incoming > top, pop top. 
                incoming < top: break
            */
            if (collisions.empty()){
                collisions.push_back(asteroids[i]);
                continue;
            }

            bool curr_dir = asteroids[i] > 0 ? true : false;
            bool prev_dir = collisions[collisions.size() - 1] > 0 ? true : false;

            if (curr_dir == prev_dir || (curr_dir == true && prev_dir == false)){
                collisions.push_back(asteroids[i]);
                continue;
            }

            int size = std::abs(asteroids[i]);

            while (true){
                int prev = std::abs(collisions[collisions.size() - 1]);
                prev_dir = collisions[collisions.size() - 1] > 0 ? true : false;

                if (curr_dir == prev_dir || (curr_dir == true && prev_dir == false)){
                    collisions.push_back(asteroids[i]);
                    break;
                }

                if (prev == size){
                    collisions.pop_back();
                    break;
                }
                else if (prev < size){
                    collisions.pop_back();

                    if (collisions.empty()){
                        collisions.push_back(asteroids[i]);
                        break;
                    }
                }

                else break;
            }
        }
        return collisions;
    }
};