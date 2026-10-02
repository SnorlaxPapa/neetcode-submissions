class Solution {
public:
    std::string simplifyPath(std::string path) {
        std::string res = "/";
        std::string dots = "";

        for (std::size_t i = 0; i < path.size(); ++i){
            dots = "";
            if (res.back() == '/' && path[i] == '.'){
                while (i < path.size() && path[i] == '.'){
                    dots += '.';
                    ++i;
                }
                --i;
                if (i + 1 < path.size() && path[i + 1] != '/'){
                    res += dots;
                    continue;
                }

                if (dots.size() == 1) continue;

                else if (dots.size() == 2){
                    if (res.size() == 1) continue;

                    res.pop_back(); //get rid of the prev /
                    while (res.back() != '/'){
                        res.pop_back();
                    }
                }
                else res += dots;
            }

            else if (path[i] == '/'){
                if (res.back() == '/') continue;
                res += '/';
            }
            else{
                res += path[i];
            }
        }

        if (res.back() == '/' && res.size() > 1) res.pop_back();
        return res;
    }
};