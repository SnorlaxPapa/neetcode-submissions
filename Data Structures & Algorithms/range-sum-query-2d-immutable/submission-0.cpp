
class NumMatrix {
private:
    std::vector<vector<int>> prefixSum;
public:
    NumMatrix(std::vector<std::vector<int>>& matrix) {
        int rows = matrix.size();
        int cols = matrix[0].size();
        prefixSum.resize(rows, std::vector<int>(cols, 0));

        int left, top, overlap;
        for (int row = 0; row < rows; ++row){
            for (int col = 0; col < cols; ++col){
                top = (row - 1) >= 0 ? prefixSum[row - 1][col] : 0;
                left = (col - 1) >= 0 ? prefixSum[row][col - 1]: 0;
                overlap = row > 0 && col > 0 ? prefixSum[row - 1][col - 1] : 0;
                prefixSum[row][col] = matrix[row][col] + top + left - overlap;
            }
            
        }
    }
    
    int sumRegion(int row1, int col1, int row2, int col2) {
        //block in a bigger block, get 4 edges
        int total = prefixSum[row2][col2];
        int top = row1 > 0 ? prefixSum[row1 - 1][col2] : 0;
        int left = col1 > 0 ? prefixSum[row2][col1 - 1] : 0;

        int overlap = row1 > 0 && col1 > 0 ? prefixSum[row1 - 1][col1 - 1] : 0;
        return total - top - left + overlap;
    }
};

/**
 * Your NumMatrix object will be instantiated and called as such:
 * NumMatrix* obj = new NumMatrix(matrix);
 * int param_1 = obj->sumRegion(row1,col1,row2,col2);
 */