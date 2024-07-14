inital_invesment = 128000 # inital invesment, implement input in next change.
quarterly_dividend = 0.61 * 80 # dividend per share * share price, implement inputs in next change.
investment_amount = inital_investment 

quarters = 0
while investment_amount < 1000000: # replace 1,000,000 with input.
  reinvestment_dividend = investment_amount / 80 * 0.61
  investment_amount += reinvestment_dividend
  quarters += 1
  years = quarters /4
print("Numbers of years to reach $1,000,000:",years)
print("Numbers of quarters to reach $1,000,000:"quarters)
print("how big the reinvesment dividend is at $1,000,000:"reinvesment_dividend)
