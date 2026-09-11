class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = float(inf)
        maxprice = 0

        for i in range (len(prices)):
            if (prices[i] < minprice):
                minprice = prices[i]

            elif (prices[i] - minprice > maxprice):
                maxprice = prices[i] - minprice

        return maxprice            
        