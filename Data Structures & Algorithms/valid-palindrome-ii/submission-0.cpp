class Solution {
private:
    bool isPalindrome(int left, int right, std::string& s){
        if (left < 0 or right >= s.size()) return false; 
        while (left < right){
            if (s[left] != s[right]) return false;
            ++left;
            --right;
        }

        return true;
    }

public:
    bool validPalindrome(std::string s) {
        int left, right;
        left = 0;
        right = static_cast<int>(s.size()) - 1;

        while (left < right){
            //skip left first
            if (s[left] != s[right]) return isPalindrome(left + 1, right, s) || isPalindrome(left, right - 1, s);
            ++left;
            --right;
        }

        return true;
    }
};