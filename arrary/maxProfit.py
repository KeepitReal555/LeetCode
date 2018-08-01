class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buyPrice = 0
        sellPrice = 0
        brought = 0
        sold = 0
        margin = 0  # 利润
        for index, item in enumerate(prices):
            # if index==0:
            #     buyPrice = prices[index] if (prices[index] < prices[index+1])
            # else:
            #     if prices[index] < prices[index+1]:
            #         buyPrice = prices[index]
            #     if prices[index] > prices[index+1]

            if index==0:
                buyPrice = prices[index] if prices[index] < prices[index + 1] else 0
                brought=1
            else:
                if index<len(prices) - 1 & prices[index] < prices[index+1] & sold == 0:
                    buyPrice = item
                    print('BuyPrice:', end=""); print(buyPrice)
                    brought = 1
                elif prices[index] > prices[index - 1] & prices[index] > prices[index + 1] & brought == 1:
                    sellPrice = item
                    print('SellPrice:', end=""); print(sellPrice)
                    margin +=  sellPrice - buyPrice
                    buyPrice = 0
                    brought = 0
                    sold =1
                elif index==len(prices) - 1 & sold==0:
                    margin = 0
                elif index == len(prices) - 1 & brought == 1:
                    sellPrice = item
                    margin += sellPrice - buyPrice
        print(margin)