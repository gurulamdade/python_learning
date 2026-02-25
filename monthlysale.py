monthly_sales = (250000, 300000, 280000, 350000, 400000, 420000)
print("January Sales:", monthly_sales[0])
print("June Sales:", monthly_sales[5])
print("Total Months:", len(monthly_sales))

# Print first 3 months sales
first_three = monthly_sales[:3]
print("First 3 months sales:", first_three)

# Print last 2 months sales
last_two = monthly_sales[-2:]
print("Last 2 months sales:", last_two)

# Count how many times 300000 appears
count_300000 = monthly_sales.count(300000)
print("Count of 300000:", count_300000)

next_quarter = (450000, 470000, 500000)
full_year_sales = monthly_sales + next_quarter
print(full_year_sales)
bonus_month = (100000,)
print(bonus_month * 3)
