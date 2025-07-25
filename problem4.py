def minimize_loss(prices):
    min_loss = float('inf')
    buy_year = sell_year = -1
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[j] < prices[i]:
                loss = prices[i] - prices[j]
                if loss < min_loss:
                    min_loss = loss
                    buy_year, sell_year = i+1, j+1
    return buy_year, sell_year, min_loss

# Example usage
prices = [20, 15, 7, 2, 13]
print(minimize_loss(prices))  # Output: (2, 5, 2)
