stock_prices = {"AAPL": 180, "TSLA": 250, "GOOGL": 150, "AMZN": 190, "MSFT": 420}

total = 0
n = int(input("Enter number of stocks: "))

for i in range(n):
    name = input("Enter stock name: ").upper()
    qty = int(input("Enter quantity: "))
    if name in stock_prices:
        total += stock_prices[name] * qty
    else:
        print("Stock not found")

print(f"Total Investment: ${total}")

# Save to file
with open("portfolio.txt", "w") as f:
    f.write(f"Total Investment: ${total}")
