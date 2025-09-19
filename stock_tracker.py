import csv
import os

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "AMZN": 135,
    "MSFT": 310,
    "GOOGL": 140
}

# Dictionary to store portfolio
portfolio = {}

print(" Welcome to Stock Portfolio Tracker!")
print("Available stocks:", ", ".join(stock_prices.keys()))

while True:
    stock = input("\nEnter stock symbol (or 'done' to finish): ").upper()

    if stock == "DONE":
        break
    elif stock not in stock_prices:
        print("❌ Invalid stock symbol. Try again!")
        continue

    try:
        quantity = int(input(f"Enter quantity of {stock}: "))
        portfolio[stock] = portfolio.get(stock, 0) + quantity
    except ValueError:
        print("❌ Please enter a valid number for quantity.")

# Calculate total investment
total_value = 0
print("\n Your Portfolio Summary:")
print("-" * 40)

for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = qty * price
    total_value += value
    print(f"{stock} - {qty} shares × ${price} = ${value}")

print("-" * 40)
print(f" Total Investment Value: ${total_value}")

# Ask user how they want to save
choice = input("\nDo you want to save as CSV or TXT? (csv/txt): ").lower()

if choice == "csv":
    with open("portfolio.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Stock", "Quantity", "Price", "Value"])
        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            value = qty * price
            writer.writerow([stock, qty, price, value])
        writer.writerow(["Total", "", "", total_value])
    print(f" Portfolio saved as {os.path.abspath('portfolio.csv')}")

elif choice == "txt":
    with open("portfolio.txt", "w") as file:
        file.write(" Portfolio Summary\n")
        file.write("-" * 40 + "\n")
        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            value = qty * price
            file.write(f"{stock} - {qty} shares × ${price} = ${value}\n")
        file.write("-" * 40 + "\n")
        file.write(f"✅ Total Investment Value: ${total_value}\n")
    print(f" Portfolio saved as {os.path.abspath('portfolio.txt')}")

else:
    print(" No file saved. (You must type 'csv' or 'txt')")
