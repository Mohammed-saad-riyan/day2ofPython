print("Welcome to the tip calculator")
bill = float(input("What was your total bill? "))
tip_percentage = float(input("What percentage tip would you like to give? 10, 12, or 15 ")) 
split = float(input("How many people to split the bill? "))
total = (tip_percentage / 100) * bill + bill
split_bill = round(total / split, 2)
print (f"Each person should pay {split_bill}")
