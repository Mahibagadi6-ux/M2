from datetime import date
from currency_converter import CurrencyConverter
c = CurrencyConverter()
print(c.convert(100,"EUR","INR",date=date(2025, 9, 1)))
atm = float(input("\nEnter the amount in USD :>>"))
new_atm = c.convert(atm,"USD","INR",date=date(2025, 8, 13))
print(new_atm)
