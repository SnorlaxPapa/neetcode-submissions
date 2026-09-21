class Solution {
public:
    int maxProfit(vector<int>& prices) {
        /*
        states:
        on day i if not holding a stock:
        1) price[i + 1] > price[i], buy & can sell for profit tmrw. we can safely make this option as we are guaranteed to make more $$
        2) if price[i + 1] <= price[i], don't buy, lower price. we can safely make this option as we can get the stock at a lower price and sell for greater profit if there is fixed x > price[i] > price[i + 1] in the future

        on day i if holding a stock:
        1) price[i + 1] > price[i], don't sell, hold onto tomorrow . we can safely make this option for more $$
        2) price[i + 1] <= price[i], sell today. if there is some x > price[i] > price[i + 1] in the future, we can buy at price[i + 1] for greater profit
        */
        bool holdingStock = false;
        int profits = 0;
        prices.push_back(0);

        for (size_t i = 0; i < prices.size() - 1; ++i){
            if (holdingStock){
                if (prices[i + 1] <= prices[i]){
                    holdingStock = false;
                    profits += prices[i];
                } 
            }
            else {
                if (prices[i + 1] > prices[i]){
                    holdingStock = true;
                    profits -= prices[i];
                }
            }
        }

        return profits;
    }
};