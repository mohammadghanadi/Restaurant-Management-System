# Restaurant-Management-System

Autor: Mohammad Ghanadi, Viktor Kulikovskyi


🗂️ Overview

This project simulates a basic restaurant system where users can:
	•	Create and manage orders for different tables
	•	View existing orders
	•	Generate and save bills

The application is implemented in Python and runs in the terminal.



🔧 Features
	•	Table-based order management
	•	Add and remove products from orders
	•	Support for special requests (e.g. “extra cheese”)
	•	Automatic bill calculation
	•	Bill export to a file
	•	Input validation and error handling



🛠 Tech Stack
	•	Python 3.x
	•	CSV file handling





🥨 Main Menu Options
Option 1 - Enter Order

Select a table number
The table is created automatically if it doesn't exist
Choose products from the displayed menu
Add special requests by typing "Extra" (adds €1 to the price)
Enter 0 when finished adding items
Option 2 - View Order

Enter the table number
All orders for the selected table are displayed
Option 3 - Invoice

Enter the table number
The invoice is calculated and saved to a text file
The invoice includes all ordered items and the total price
Option 0 - Exit Restaurant

Terminates the program
Features

Order Management

Orders are managed separately for each table
Support for special requests (extras)
Multiple items per order
Real-time order display
Invoice System

Automatic invoice calculation
Invoices are saved to text files
Includes itemized breakdown and total price
Persistent storage
Error Handling

The program automatically handles:

Invalid Input: User is prompted to enter valid data
Table/Product Not Found: Appropriate error message is displayed
File Not Found: Error message when saving invoices to non-existent directories
System Architecture

The program consists of three main classes:

Table - Represents a restaurant table and manages its orders
Product - Represents a menu item (dish, side, beverage) with price and properties
Main_menu - Manages user interaction and orchestrates all program functions
Known Issues

🚧 No known bugs have been found when all inputs are correctly entered with the expected data types.

Testing

The program includes automatic test cases for:

Product creation
Table creation
Order processing
Order display
Invoice generation
