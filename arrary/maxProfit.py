class Solution:
    def maxProfitSelf(self, prices):
        """
        设定历史最高价格和历史最低价格，与现在遍历的价格比较决定买卖,此方法太繁琐
        :type prices: List[int]
        :rtype: int
        """
        length = len(prices)
        maxPrice = 0
        minPrice = 99999999999
        flag = 0    # 是否持有股票的标注, 0为未持有，1为持有
        margin = 0 # 利润

        for index, item in enumerate(prices):
            if index==length-1:
                if flag == 0:
                    margin = margin
                else:
                    maxPrice = item
                    margin += maxPrice - minPrice
                    maxPrice = 0
                    minPrice = 99999999999
                    flag = 0
            else:
                if flag == 0: # 未持有股票，判断此时是否应该购买股票
                    if item <= minPrice: # 比历史价格低，设置新的历史价格
                        minPrice = item
                        if prices[index+1]>minPrice :
                            flag = 1 #购入
                else:   # 持有股票，判断此时应该卖出股票
                    if item >= maxPrice:
                        maxPrice = item
                        if prices[index+1] < maxPrice:
                            margin += maxPrice - minPrice
                            maxPrice = 0
                            minPrice = 99999999999
                            flag = 0
        print(margin)
        return margin

    def maxProfit(self, prices):
        '''
        简洁的方法，源自答案
        :param prices:
        :return:
        '''
        minPrice = prices[0]
        margin = 0
        if len(prices)<2:
            margin = 0
        for i in range(1, len(prices)):
            if prices[i-1] < prices[i]:
                margin += int(prices[i]) - int(prices[i-1])

        print(margin)
        return margin


sol = Solution()
list = [7,6,4,3,1]
sol.maxProfit(list)

