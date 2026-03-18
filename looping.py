orders= [2500, 1200, 5000, 800, 3200, 1500]

total_revenue=0
high_value_orders=0
max_order=0
min_order=0
average=()

for order in orders:
  total_revenue = total_revenue + order
  
  if order > 2000:
    high_value_orders = high_value_orders + 1
    
  if order > max_order:
    max_order = order

  if order < min_order:
    min_order = order  

  if order < min_order:
    average / order
    
 
    
print("Total Revenue:", total_revenue)
print("Orders Above 2000:", high_value_orders)
print("Highest Order:", max_order)
print("Minimum order:",min_order)
print("average order:",average)
