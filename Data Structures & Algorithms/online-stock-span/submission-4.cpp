class StockSpanner {
private:
    std::vector<std::vector<int>> priceStack; 

public:
/*consecutive previous, means if we encounter a higher price, subsequent prices must have higher price to be included in span. so if we encounter lower price than current, return 1. if not we can keep popping until we get a higher price and include popped spans into curr. monotically decreasing*/
    StockSpanner() {
        priceStack.push_back({-1, 0});
    }
    
    int next(int price) {
        if (price < priceStack.back()[0]){
            priceStack.push_back({price, 1});
            return 1;
        }
        
        int span = 1;
        while (!priceStack.empty() && price >= priceStack.back()[0]){
            span += priceStack.back()[1];
            priceStack.pop_back();
        }

        priceStack.push_back({price, span});
        return span;

    }
};

/**
 * Your StockSpanner object will be instantiated and called as such:
 * StockSpanner* obj = new StockSpanner();
 * int param_1 = obj->next(price);
 */