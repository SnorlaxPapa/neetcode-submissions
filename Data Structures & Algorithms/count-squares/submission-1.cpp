#include <unordered_map>
#include <vector>
class CountSquares {
public:
    std::unordered_map<int, std::unordered_map<int, int>> pointFreq;
    CountSquares() {
    }
    
    void add(std::vector<int> point) {
        pointFreq[point[0]][point[1]]++;
    }

    
    int count(std::vector<int> point) {
        int x = point[0];
        int y = point[1];

        int x2Count, x3Count, x4Count;
        int num_squares = 0;

        for (const auto& [xOther, ymap]: pointFreq){
            if (xOther == x) continue;
            for (const auto& [yOther, count]: pointFreq[xOther]){
                if (yOther == y) continue;

                x2Count = count;
                x3Count = pointFreq[xOther][y];
                x4Count = pointFreq[x][yOther];
                num_squares += x2Count * x3Count * x4Count;
            }
        }
        return num_squares;
    }
};
