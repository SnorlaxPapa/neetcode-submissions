class StockSpanner {
private:
    std::vector<std::vector<int>> priceStack; 

public:
    /*
    consecutive days
    when we push in a price, we keep popping the top if the top > curr price 
    but we need to preserve for future elements that > both. 
    instead we can pop the top, then push it back once done
    that means we can implement a monotonic increasing stack
    */
    StockSpanner() {
        priceStack.push_back({-1, 0});
    }
    
    int next(int price) {
        if (price < priceStack.back()[0]){
            priceStack.push_back({price, 1});
            return 1;
        }
        
        int span = 1;
        while (!priceStack.empty() and price >= priceStack.back()[0]){
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