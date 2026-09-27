#include <string>

class Solution {
public:
    int calPoints(std::vector<string>& operations) {
        std::vector<int> score;
        int num;
        score.reserve(operations.size());
        std::size_t n;
        
        for (const string& op: operations){
            n = score.size() - 1;
            if (op == "+"){
                score.push_back(score[n] + score[n - 1]);
            }
            else if (op == "D"){
                score.push_back(score[n] * 2);
            }
            else if (op == "C"){
                score.pop_back();
            }
            else{
                num = std::stoi(op);
                score.push_back(num);
            }
        }
        
        int res = 0;
        for (const int& x: score){
            res += x;
        }

        return res;
    }
};