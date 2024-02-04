def maxProfit(stocks):
    l, r = 0, 1
    maxP = float("-inf")
    buy_price, sell_price = 0, 0
    
    while r < len(stocks):
        if stocks[r] > stocks[l]:
            current_profit = stocks[r] - stocks[l]
            if current_profit > maxP:
                maxP = current_profit
                buy_price, sell_price = stocks[l], stocks[r]
        else:
            l = r
        
        r += 1
    
    return maxP, buy_price, sell_price

stocks = [9, 7, 10, 6, 45, 1, 5]
result = maxProfit(stocks)
print("Maximum Profit:", result[0])
print("Buy Price:", result[1])
print("Sell Price:", result[2])
	

def maxProfitMultipleTransactions(stocks):
    total_profit = 0
    
    for i in range(1, len(stocks)):
        if stocks[i] > stocks[i - 1]:
            total_profit += stocks[i] - stocks[i - 1]
    
    return total_profit

stocks = [9, 7, 10, 6, 45, 1, 5]
result = maxProfitMultipleTransactions(stocks)
print("Cumulative Maximum Profit:", result)