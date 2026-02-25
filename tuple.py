monthly_sales = (250000, 300000, 280000, 350000, 400000, 420000 )

print("january sales:", monthly_sales[0])
print("june sales:", monthly_sales[5])
print("")

print("Total Months:", len(monthly_sales))
print("")

next_quarter = (450000, 470000, 500000)
full_year_sales = monthly_sales + next_quarter  
print("Full Year Sales:", full_year_sales)
print("")

bonus_month = (100000)
print(bonus_month * 3)
print("")

print( monthly_sales[0:3])
print(monthly_sales[-1:-2])
print(300000  in monthly_sales)