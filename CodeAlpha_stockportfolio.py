# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 400,
    "AMZN": 180
}

total_investment = 0

print("Available Stocks:")
for stock in stock_prices:
    print(stock, "₹", stock_prices[stock])

print("\nEnter 'done' when you are finished.")

while True:
    stock_name = input("\nEnter stock name: ").upper()

    if stock_name == "DONE":
        break

    if stock_name not in stock_prices:
        print("Stock not available.")
        continue

    quantity = int(input("Enter quantity: "))

    price = stock_prices[stock_name]
    investment = price * quantity

    total_investment += investment

    print(stock_name, "x", quantity, "=", "₹", investment)

print("\n----------------------------")
print("Total Investment: ₹", total_investment)
print("----------------------------")

# Save result to a text file
save = input("Do you want to save the result? (yes/no): ").lower()

if save == "yes":
    with open("portfolio.txt", "w") as file:
        file.write("Stock Portfolio Report\n")
        file.write("----------------------\n")
        file.write("Total Investment: ₹" + str(total_investment))

    print("Portfolio saved to portfolio.txt")