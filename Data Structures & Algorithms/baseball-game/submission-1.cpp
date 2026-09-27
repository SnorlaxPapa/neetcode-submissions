#include <string>

class Solution {
public:
    int calPoints(std::vector<string>& operations) {
        std::vector<int> score;
        int num, sum, res = 0;
        score.reserve(operations.size());
        std::size_t n;
        
        for (const string& op: operations){
            n = score.size() - 1;
            if (op == "+"){
                sum = score[n] + score[n - 1];
                score.push_back(sum);
                res += sum;
            }
            else if (op == "D"){
                sum = score[n] * 2;
                res += sum;
                score.push_back(sum);
            }
            else if (op == "C"){
                res -= score[n];
                score.pop_back();
            }
            else{
                num = std::stoi(op);
                score.push_back(num);
                res+=num;
            }
        }
        
        return res;
    }
};