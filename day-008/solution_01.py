def max_profit(prices):
    if len(prices) < 2:
        return 0
    
    min_price = prices[0]
    best_profit = 0

    for price in prices:
        if price - min_price > best_profit:
            best_profit = price - min_price
        if price < min_price:        
            min_price = price
    return best_profit

print(max_profit([7, 1, 5, 3, 6, 4])) # 5
print(max_profit([7, 6, 4, 3, 1])) # 0
print(max_profit([1, 2, 3, 4, 5])) # 4
print(max_profit([2, 4, 1])) # 2
print(max_profit([3, 3, 3, 3])) # 0
print(max_profit([5])) # 0
print(max_profit([])) # 0