initial_investment = float(input("Enter your initial investment : ")) # initial investment
quarterly_dividend = float(input("Enter quarterly dividend : "))
stock_price = float(input("Enter stock price : "))
investment_amount = initial_investment 
investment_goal = float(input("Enter your investment goal : "))

quarters = 0
while investment_amount < investment_goal:
  reinvestment_dividend = investment_amount / stock_price * quarterly_dividend   # dividend per share * share price
  investment_amount += reinvestment_dividend
  quarters += 1
  years = quarters / 4
print("Number of years to reach", investment_goal,":", years)
print("Number of quarters to reach", investment_goal,":", quarters)
print("How big the reinvestment dividend, is at", investment_goal,":", reinvestment_dividend)
