# ---------------------------------------------
# Simple Railway Ticket Booking System
# ---------------------------------------------

trains = [
    {"train_no": 101, "name": "Express A", "seats": 5, "fare": 150},
    {"train_no": 202, "name": "Express B", "seats": 3, "fare": 200},
    {"train_no": 303, "name": "Superfast C", "seats": 2, "fare": 250}
]

bookings = []   # stores booking details (no file used)


def show_trains():
    print("\nAvailable Trains:")
    print("------------------------------------")
    for t in trains:
        print(f"Train No: {t['train_no']} | Name: {t['name']} | Seats: {t['seats']} | Fare: ₹{t['fare']}")
    print("------------------------------------")


def book_ticket():
    show_trains()
    train_no = int(input("Enter Train Number to book: "))

    # find selected train
    train = next((t for t in trains if t["train_no"] == train_no), None)

    if train is None:
        print("Invalid Train Number!")
        return

    if train["seats"] <= 0:
        print("No seats available!")
        return

    name = input("Enter Passenger Name: ")
    age = int(input("Enter Age: "))

    # booking confirmed
    train["seats"] -= 1
    ticket = {
        "passenger": name,
        "age": age,
        "train_no": train_no,
        "fare": train["fare"]
    }
    bookings.append(ticket)

    print("\n🎉 Ticket Successfully Booked!")
    print("------------------------------------")
    print(f"Passenger: {name}")
    print(f"Train: {train['name']} ({train['train_no']})")
    print(f"Fare: ₹{train['fare']}")
    print("------------------------------------")


def view_bookings():
    if not bookings:
        print("\nNo bookings yet!")
        return

    print("\nYour Bookings:")
    print("------------------------------------")
    for b in bookings:
        print(f"Passenger: {b['passenger']} | Train No: {b['train_no']} | Fare: ₹{b['fare']}")
    print("------------------------------------")


def main_menu():
    while True:
        print("\n=== Railway Ticket Booking System ===")
        print("1. View Available Trains")
        print("2. Book a Ticket")
        print("3. View All Bookings")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            show_trains()
        elif choice == "2":
            book_ticket()
        elif choice == "3":
            view_bookings()
        elif choice == "4":
            print("Thank you for using the system!")
            break
        else:
            print("Invalid choice!")


# Run the program
main_menu()
