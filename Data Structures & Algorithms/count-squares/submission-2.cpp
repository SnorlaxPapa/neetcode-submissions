#include <unordered_map>
#include <vector>
class CountSquares {
private:
    std::unordered_map<int, std::unordered_map<int, int>> pointFreq;
    int getFrequency(int x, int y){
        auto xIt = pointFreq.find(x);
        if (xIt == pointFreq.end()) return 0;

        auto yIt = xIt->second.find(y);
        if (yIt == xIt->second.end()) return 0;

        return yIt->second;
    }
public:
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
                if (std::abs(xOther - x) != std::abs(yOther-y)) continue;

                x2Count = count;
                x3Count = getFrequency(xOther, y);
                x4Count = getFrequency(x, yOther);
                num_squares += x2Count * x3Count * x4Count;
            }
        }
        return num_squares;
    }
};
