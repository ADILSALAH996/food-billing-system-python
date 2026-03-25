**Food Billing System (Python Tkinter)**

A desktop-based restaurant billing system built using Python and Tkinter.
This application allows users to select menu items, calculate totals with service charge, discount, and GST, generate formatted receipts, and automatically save billing records.

**Features**
Menu-based food and drink selection
Quantity control using ➕ and ➖ buttons
Automatic billing calculations
Service charge calculation
Discount support (0–90%)
GST tax calculation
Professional receipt generation
Unique receipt number generation
Automatic receipt saving
Manual backup saving
Reset functionality
Input validation for safety
Read-only billing fields (prevents tampering)
Modern UI layout
**Billing Logic Used**

The billing process follows realistic restaurant billing:

Calculate total items cost
Add service charge
Apply discount
Calculate GST
Generate final total

This ensures correct financial calculations.

**Technologies Used**
Python 3
Tkinter (GUI Development)
File Handling (Receipt Saving)
Dictionaries (Efficient Data Handling)
Date & Time Handling
Input Validation Techniques
**Requirements**
Software Requirements
Python 3.8+
Tkinter

Most Python installations include Tkinter.

If Tkinter is missing (Linux):

sudo apt install python3-tk
Hardware Requirements
Processor: Any modern CPU
RAM: Minimum 2 GB
Disk Space: ~50 MB
Display Resolution: 1024×768 or higher
**How to Run the Project**

Step 1 — Clone repository:

git clone https://github.com/yourusername/Food-Billing-System.git

Step 2 — Navigate to folder:

cd Food-Billing-System

Step 3 — Run the program:

python billing_system.py
**Receipt System**

Each receipt includes:

Restaurant name
Unique bill number
Date & time
Item details
Quantity and price
Service charge
Discount amount
GST tax
Final total
Total number of items

Receipts are automatically saved in:

Receipts/

Manual backups are saved in:

Manual_Backups/
📁 Project Structure
Food-Billing-System/
│
├── billing_system.py
├── README.md
├── requirements.txt
│
├── Receipts/
├── Manual_Backups/
│
└── screenshots/

**Input Validation Features**

The system prevents:

Invalid numeric inputs
Empty GST values
Invalid discount percentages
Receipt generation before calculation

This improves reliability and prevents crashes.

**Testing Done**

Tested with:

Zero quantity inputs
Large quantity values
Invalid numeric entries
Empty GST field
Multiple receipt generations

All scenarios handled safely.

**Future Improvements**

Possible enhancements:

Database integration (SQLite/MySQL)
Daily sales reports
Inventory management
Print-to-PDF feature
Multi-user login system
Payment methods (Cash/Card/UPI)

These would move it toward real POS systems.

**Learning Outcomes**

This project demonstrates:

GUI development using Tkinter
Real-world billing logic
Error handling and validation
File handling in Python
Structured program design
User-friendly interface design
**Author**

Adil Salah
