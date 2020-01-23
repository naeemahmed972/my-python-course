

# Write a Python Program to Convert the Given Number of Days to a Measure of Time Given in Years, Weeks and Days. For Example, 375 Days Is Equal to 1 Year, 1 Week and 3 Days (Ignore Leap Year).

# Months calculation is complicated
# Ignoring Leap years, number of days in a year = 365

# 1 year = 365 days => num_of_days // 365 = years
# e.g. 678 days (678/365 = 1.857..) => 678//365 = 1 year

# Remaining number of days to be converted to weeks
# How to get remainder?
# 678 % 365 = 313
# number of weeks = 313 // 7 = 44 weeks

# Remaining number is number of days
# 313 % 7 = 5 days

# So the answer should be 1 year, 44 weeks and 5 days












# number_of_days = int(input("Enter number of days: "))

# number_of_years = number_of_days // 365
# remaining_days = number_of_days % 365

# number_of_weeks = remaining_days // 7
# number_of_days = remaining_days % 7

# print(f"{number_of_years} year(s), {number_of_weeks} week(s) and {number_of_days} day(s)")