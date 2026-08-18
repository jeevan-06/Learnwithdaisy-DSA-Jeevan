class Solution:
    def maxProfit(self,prices):
        best_buy=prices[0]
        max_profit=0
        
        for price in prices:
            if price<best_buy:
                best_buy=price
            
            profit=price-best_buy

            if profit>max_profit:
                max_profit=profit

        return max_profit
