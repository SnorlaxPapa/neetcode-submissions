#include <vector>

class Solution {
public:
    std::string multiply(std::string num1, std::string num2) {
        std::vector<int> res(num1.size() + num2.size());

        if (num1 == "0" or num2 == "0") return "0";
        std::reverse(num1.begin(), num1.end());
        std::reverse(num2.begin(), num2.end());
        int digit1, digit2, product;

        for (std::size_t i = 0; i < num1.size(); ++i){
            digit1 = num1[i] - '0';
            for (std::size_t j = 0; j < num2.size(); ++j){
                digit2 = num2[j] - '0';
                product = digit1 * digit2;

                res[i + j] += product;
                res[i + j + 1] += res[i + j] / 10;
                res[i + j] %= 10; 
            }
        }  

        std::reverse(res.begin(), res.end());
        size_t begin = 0;
        while (begin < res.size() && res[begin] == 0){
            begin += 1;
        }

        
        std::string result = "";
        for (std::size_t i = begin; i < res.size(); ++i){
            result.push_back(res[i] + '0');
        }

        return result;
        
    }
};
