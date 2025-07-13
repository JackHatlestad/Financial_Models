import yfinance as yf 
import pandas as pd 

def add_stock(df):
    while True:
        ticker = input("What stock do you want to add? \n")
        shares = int(input("How many shares do you want to buy? \n"))

        if ticker in 



def view_portfolio(df):
    print("Portfolio Stats")

def advanced_stats(df1):
    print("Advanced_Stats")


def main():
    username = input("Enter username: ")
    try:
        df = pd.read_excel(f"{username}.xlsx")
    except FileNotFoundError:
        df = pd.DataFrame(columns=["Ticker Symbol", 'Current Balance', 'Shares', 'Current Price', 'Expense Ratio'])
    try:
        df1 = pd.read_excel(f"{username}'1'.xlsx")
    except FileNotFoundError:
        df1 = pd.DataFrame(columns=["% Stocks", '% Bonds', '% Others', '% Domestic Stocks', '% International Stocks',
                                    'Investment Costs'])
        

    
    while True: 
        menu = int(input("1. Add Stock\n 2. View Portfolio \n 3. Advanced Portfolio Statistics \n 4. Exit \n"))
        if menu == 1:
            add_stock(df)
    
        elif menu == 2:
            view_portfolio(df)
    
        elif menu == 3:
            advanced_stats(df1)
    
        elif menu == 4: 
            print("Exiting...")
            df.to_excel(f"{username}.xlsx", index=False)
            df.to_excel(f"{username}'1'.xlsx", index=False)
            break
    
        else:
            print("Error: choose 1,2,3")

if __name__ == "__main__":
    main()
