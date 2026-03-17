age = 78  

if age < 12:
    print("Ticket Price: 100")
elif age <= 60:
    # Standard price is 200, applying a 20% discount
    print("Ticket Price: 160")
else:
    # Modified price for Senior Citizens (above 60)
    print("Senior Citizen -> Price: 120")
    