class Solution {
public:
    string decodeString(string s) {
        /*we maintain two stacks, one with the previous strings and the correspoding with the count of the string we are currently working through
        when we encounter an open bracket, we first preserve our string we are currently on, and add the number of times we need to repeat the string we will proceed to work on. then, when we encounter.a closed bracket, we simply repeat whatever current string we have based on the previously saved k and concat it to the prev string

        e.g. for 

        a2[3[b]c4[d]]
        a added to cur
        2 -> k = 2
        open bracket, 
        stack with a, count 2 for subsequent string, reset k and current string
        3 -> k = 3,
        open bracket,
        stack with "", count 3 for subsequent string, reset k
        b, add to curr
        closed bracket, pop previous curr ("") and add b to it 3 times. 

        repeat down the string

        we do one pass down the string, with k repeats for each integer, which means we have O(n + N) time where n is the len of the input string and N is the length of the output string with O(n) auxiliary space
        */
        std::vector<std::string> stringStack;
        std::vector<int> countStack;
        int k = 0, count;
        std::string cur = "";

        for (std::size_t i = 0; i < s.size(); ++i){
            if (isdigit(s[i])){
                k = k * 10 + (s[i] - '0');
            }else if (s[i] == '['){
                stringStack.push_back(cur);
                countStack.push_back(k);
                cur = "";
                k = 0;
            }else if (s[i] == ']'){
                std::string tmp = cur;
                cur = stringStack.back();
                count = countStack.back();

                stringStack.pop_back();
                countStack.pop_back();

                while (count-- > 0){
                    cur += tmp;
                }
            }else {
                cur += s[i];
            }
        }

        return cur;
    }
};