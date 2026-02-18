# HOTEL MANAGEMENT SYSTEM
# Console Based - Only Python

import os

FILENAME = "hotel_data.txt"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def pause():
    input("\nPress Enter to continue...")

def add_customer():
    clear()
    print("----- ADD NEW CUSTOMER -----")
    name = input("Customer Name: ")
    phone = input("Phone Number: ")
    address = input("Address: ")

    with open(FILENAME, "a") as f:
        f.write(f"CUSTOMER|{name}|{phone}|{address}\n")

    print("\nCustomer added successfully!")
    pause()

def book_room():
    clear()
    print("----- ROOM BOOKING -----")
    name = input("Customer Name: ")
    room_no = input("Room Number: ")
    days = int(input("Number of Days: "))
    rate = int(input("Rate per Day: "))

    total = days * rate

    with open(FILENAME, "a") as f:
        f.write(f"BOOKING|{name}|{room_no}|{days}|{rate}|{total}\n")

    print("\nRoom booked successfully!")
    pause()

def view_customers():
    clear()
    print("----- CUSTOMER DETAILS -----")

    if not os.path.exists(FILENAME):
        print("No data found.")
        pause()
        return

    with open(FILENAME, "r") as f:
        found = False
        for line in f:
            if line.startswith("CUSTOMER"):
                found = True
                data = line.strip().split("|")
                print(f"\nName    : {data[1]}")
                print(f"Phone   : {data[2]}")
                print(f"Address : {data[3]}")

        if not found:
            print("No customers found.")

    pause()

def view_bookings():
    clear()
    print("----- ROOM BOOKINGS -----")

    if not os.path.exists(FILENAME):
        print("No data found.")
        pause()
        return

    with open(FILENAME, "r") as f:
        found = False
        for line in f:
            if line.startswith("BOOKING"):
                found = True
                data = line.strip().split("|")
                print("\nCustomer Name :", data[1])
                print("Room Number   :", data[2])
                print("Days          :", data[3])
                print("Rate per Day  :", data[4])
                print("Total Amount  :", data[5])

        if not found:
            print("No bookings found.")

    pause()

def generate_bill():
    clear()
    print("----- GENERATE BILL -----")
    name = input("Enter Customer Name: ")

    if not os.path.exists(FILENAME):
        print("No data found.")
        pause()
        return

    with open(FILENAME, "r") as f:
        found = False
        for line in f:
            if line.startswith("BOOKING"):
                data = line.strip().split("|")
                if data[1].lower() == name.lower():
                    found = True
                    print("\n----- BILL -----")
                    print("Customer Name :", data[1])
                    print("Room Number   :", data[2])
                    print("Days          :", data[3])
                    print("Rate per Day  :", data[4])
                    print("Total Amount  :", data[5])

        if not found:
            print("Booking not found for this customer.")

    pause()

def main_menu():
    while True:
        clear()
        print("================================")
        print("     HOTEL MANAGEMENT SYSTEM    ")
        print("================================")
        print("1. Add New Customer")
        print("2. Book Room")
        print("3. View Customer Details")
        print("4. View All Bookings")
        print("5. Generate Bill")
        print("6. Exit")
        print("================================")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_customer()
        elif choice == "2":
            book_room()
        elif choice == "3":
            view_customers()
        elif choice == "4":
            view_bookings()
        elif choice == "5":
            generate_bill()
        elif choice == "6":
            print("\nThank you for using Hotel Management System!")
            break
        else:
            print("\nInvalid choice!")
            pause()

# Run Program
main_menu()