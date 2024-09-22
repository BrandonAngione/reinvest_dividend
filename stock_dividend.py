question = input("What goal would you like to set? invest_goal or dividend_goal: ").lower().strip()
initial_investment = float(input("Enter your initial investment: "))  # Initial investment
quarterly_dividend = float(input("Enter quarterly dividend: "))
stock_price = float(input("Enter stock price: "))
investment_amount = initial_investment

quarters = 0 

if question == "invest_goal":
    investment_goal = float(input("Enter your investment goal: "))
    while investment_amount < investment_goal:
        reinvestment_dividend = investment_amount / stock_price * quarterly_dividend  # Dividend per share * share price
        investment_amount += reinvestment_dividend
        quarters += 1
    years = quarters / 4  # Calculate years after the loop
    print("Number of years to reach", investment_goal, ":", years)
    print("Number of quarters to reach", investment_goal, ":", quarters)
    print("Reinvestment dividend at", investment_goal, ":", reinvestment_dividend)

elif question == "dividend_goal":
    dividend_goal = float(input("Enter your dividend goal: "))
    reinvestment_dividend = 0
    while reinvestment_dividend < dividend_goal:
        reinvestment_dividend = investment_amount / stock_price * quarterly_dividend  # Dividend per share * share price
        investment_amount += reinvestment_dividend
        quarters += 1
    years = quarters / 4  # Calculate years after the loop
    print("Number of years to reach", dividend_goal, ":", years)
    print("Number of quarters to reach", dividend_goal, ":", quarters)
    print("Investment amount at", dividend_goal, ":", investment_amount)

else:
    print("Invalid input, choices are invest_goal or dividend_goal")
