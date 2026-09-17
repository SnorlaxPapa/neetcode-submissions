#include <algorithm>
class Solution {
private:
    std::string findPrefix(std::string& s1, std::string& s2) const{
        std::string prefix = "";
        std::size_t size = std::min(s1.size(), s2.size());

        for (std::size_t i = 0; i < size; ++i){
            if (s1[i] == s2[i]){
                prefix.push_back(s1[i]);
            }
            else break;
        }

        return prefix;
    }

public:
    std::string longestCommonPrefix(std::vector<std::string>& strs) {
        std::string prefix = strs[0];

        for (std::size_t i = 1; i < strs.size(); ++i){
            prefix = findPrefix(prefix, strs[i]);
            
            if (prefix == "") return prefix;
        }

        return prefix;
    }
};