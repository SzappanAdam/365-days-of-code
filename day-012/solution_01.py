def max_profit_multiple(prices):
    profit = 0

    for i in range(len(prices)-1):
        if prices[i] < prices[i+1]:
            profit += prices[i+1] - prices[i]
    return profit

print(max_profit_multiple([7, 1, 5, 3, 6, 4])) # 7
print(max_profit_multiple([1, 2, 3, 4, 5])) # 4
print(max_profit_multiple([7, 6, 4, 3, 1])) # 0
print(max_profit_multiple([1, 5, 2, 8])) # 10
print(max_profit_multiple([3, 3, 3, 3])) # 0
print(max_profit_multiple([2, 4, 1, 7])) # 8
print(max_profit_multiple([5])) # 0
print(max_profit_multiple([])) # 0