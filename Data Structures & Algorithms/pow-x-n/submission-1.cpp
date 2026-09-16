class Solution {
public:
    double myPow(double x, int n) {
        /*
        x^n = x^n-1 * x = x^n-n//2 * x^n//2
        div and conquer power
        */
        if (n == 1){
            return x;
        }
        if (n == -1){
            return 1/x;
        }
        if (n == 0){
            return 1;
        }

        int half = n/2;
        double res = myPow(x, half);
        res *= res;
        if (n % 2 == 0) return res;
        if (n > 0) return res * x;
        return res / x;
    }
};
