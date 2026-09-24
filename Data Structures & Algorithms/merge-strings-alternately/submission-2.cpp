class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        std::size_t i = 0, j = 0;
        std::string s = "";
        s.reserve(word1.size() + word2.size());
        int counter = 0;
        while (true){
            if (j == word2.size()){
                while (i < word1.size()){
                    s += word1[i];
                    ++i;
                }
                break;
            }

            if (i == word1.size()){
                while (j < word2.size()){
                    s += word2[j];
                    ++j;
                }
                break;   
            }

            if (counter % 2 == 0){
                s += word1[i];
                ++i;
            }

            else{
                s += word2[j];
                ++j;
            }

            ++counter;
        }
        return s;
    }
};