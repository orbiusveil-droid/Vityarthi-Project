📄 README.md — Railway Ticket Booking System
🚆 Railway Ticket Booking System

A simple console-based Python project that allows users to view trains, book tickets, and check their bookings — created according to the project objectives:
✔ Identifying a meaningful problem
✔ Designing a technical solution
✔ Implementing it using course-level tools
✔ Demonstrating understanding through working code

📌 1. Project Objective

The objective of this project is to apply subject concepts in a real-world context by:

Identifying a meaningful problem

Designing a technical solution

Implementing the solution using the tools/methods learned in the course

Demonstrating understanding through documentation and evaluation

📌 2. Problem Identification

Railway ticket booking is often done manually or using complex systems. For learning purposes, this project creates a simplified ticket booking system where:

Users can view available trains

Users can book tickets

Seat count updates automatically

Users can view all booked tickets

This simulates a real-world booking system in an easy, educational way.

📌 3. Features
✔ View Available Trains

Displays train number, name, available seats, and fare.

✔ Book a Ticket

User enters train number

Provides name and age

Seat count decreases upon booking

Ticket information is stored in memory (no files used)

✔ View All Bookings

Shows all tickets booked in the session.

✔ Menu-Driven Interface

Simple and user-friendly console menu.

✔ No File or Database

All data is stored temporarily in Python lists and dictionaries.

📌 4. Technologies Used

Python (Basic concepts: lists, loops, dictionaries, functions)

No external libraries

No database & no CRUD file operations

📌 5. How to Run the Program

Install Python 3 on your system.

Copy the code into a file named:

railway_booking.py


Run the script using Terminal / Command Prompt:

python railway_booking.py

📌 6. Code Overview
Main components:

trains → List storing train information

bookings → List storing user bookings

show_trains() → Displays available trains

book_ticket() → Handles ticket booking logic

view_bookings() → Shows all ticket bookings

main_menu() → Controls the user interface

📌 7. Sample Output
=== Railway Ticket Booking System ===
1. View Available Trains
2. Book a Ticket
3. View All Bookings
4. Exit
Enter your choice:


After booking:

🎉 Ticket Successfully Booked!
Passenger: Rahul
Train: Express B (202)
Fare: ₹200

📌 8. Limitations

Data is not saved after the program ends

No cancellation or modification

No real payment processing

These limitations keep the project simple and suitable for academic learning.

📌 9. Future Improvements (Optional)

Add PNR number generation

Add ticket cancellation feature

Save bookings in a file or database

Add classes (Sleeper/AC)

Create GUI using Tkinter

📌 10. Conclusion

This project successfully demonstrates how to:

Identify a real-world problem

Build a functional technical solution

Apply Python programming skills

Document and evaluate a working system
