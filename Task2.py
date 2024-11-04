# TASK 2 : Stock Portfolio Tracker...

class Stock:
    def __init__(self, symbol, shares, price):
        self.symbol = symbol.upper()
        self.shares = shares
        self.price = price

    def update_price(self, new_price):
        self.price = new_price

    def get_value(self):
        return self.shares * self.price

class Portfolio:
    def __init__(self):
        self.stocks = {}

    def add_stock(self, symbol, shares, price):
        if symbol in self.stocks:
            print(f"{symbol} already exists in portfolio. Updating shares and price.")
            self.stocks[symbol].shares += shares
            self.stocks[symbol].price = price
        else:
            self.stocks[symbol] = Stock(symbol, shares, price)
        print(f"Added {shares} shares of {symbol} at ${price:.2f}.")

    def remove_stock(self, symbol):
        if symbol in self.stocks:
            del self.stocks[symbol]
            print(f"{symbol} removed from portfolio.")
        else:
            print(f"{symbol} is not in your portfolio.")

    def update_stock_price(self, symbol, new_price):
        if symbol in self.stocks:
            self.stocks[symbol].update_price(new_price)
            print(f"Updated {symbol} price to ${new_price:.2f}.")
        else:
            print(f"{symbol} not found in your portfolio.")

    def display_portfolio(self):
        print("\nCurrent Portfolio:")
        for symbol, stock in self.stocks.items():
            print(f"{symbol}: {stock.shares} shares at ${stock.price:.2f} each, Total Value: ${stock.get_value():.2f}")

    def get_portfolio_value(self):
        total_value = sum(stock.get_value() for stock in self.stocks.values())
        print(f"\nTotal Portfolio Value: ${total_value:.2f}")
        return total_value

def main():
    portfolio = Portfolio()
    
    while True:
        print("\nPortfolio Menu:")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. Update Stock Price")
        print("4. Display Portfolio")
        print("5. Show Portfolio Value")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            symbol = input("Enter stock symbol: ").upper()
            shares = int(input("Enter number of shares: "))
            price = float(input("Enter stock price: "))
            portfolio.add_stock(symbol, shares, price)
        
        elif choice == "2":
            symbol = input("Enter stock symbol to remove: ").upper()
            portfolio.remove_stock(symbol)
        
        elif choice == "3":
            symbol = input("Enter stock symbol to update: ").upper()
            new_price = float(input("Enter new stock price: "))
            portfolio.update_stock_price(symbol, new_price)
        
        elif choice == "4":
            portfolio.display_portfolio()
        
        elif choice == "5":
            portfolio.get_portfolio_value()
        
        elif choice == "6":
            print("Exiting Portfolio Tracker. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()
