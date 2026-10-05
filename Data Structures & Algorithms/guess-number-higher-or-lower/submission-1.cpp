/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * int guess(int num);
 */

class Solution {
private:
    int top;
    int bottom = 1;

public:
    int guessNumber(int n) {
        top = n;

        int res = 1;
        while (true){
            int middle = bottom + (top - bottom) / 2;
            res = guess(middle);

            if (res == 0){
                return middle;
            }

            if (res == -1){
                top = middle - 1;
            }
            else {
                bottom = middle + 1;
            }
        }
    }
};