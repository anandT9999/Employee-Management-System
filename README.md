# Employee Management System

## Overview
This Employee Management System is a command-line application developed in Python that allows a company to manage information about its employees and departments using Object-Oriented Programming (OOP) principles and efficient data structures. The system provides functionalities such as adding/removing employees, adding/removing departments, displaying employee details, and more.

## Structure
- `employee_management_system.py`: The main Python script containing the implementation of the Employee Management System.
- `test_employee_management_system.py`: Optional test script with unit tests to validate the functionality of the system.

## Implementation Details

### Employee Class
- The `Employee` class represents an individual employee with attributes for name, ID, title, and department.
- It includes methods to display employee details and provide a string representation.

### Department Class
- The `Department` class represents a department within the company with attributes for the department name and a list of employees.
- It includes methods to add an employee, remove an employee, and list all employees in the department.

### Company Class
- The `Company` class represents the entire company and maintains a dictionary to store department objects.
- It includes methods to add a department, remove a department, display all departments, save data to a file, and load data from a file.

### User Interaction
- The `print_menu()` function prints a menu for user interaction with options to perform various actions.
- The `main()` function handles user inputs and executes corresponding actions based on the menu choices.

### Data Persistence (Optional)
- The system allows saving company data to a file and loading it back on startup using JSON format.

## Usage
1. Run `employee_management_system.py` using a Python interpreter.
2. Follow the menu prompts to interact with the system (e.g., add employees, add departments, etc.).
3. Optional: Use `test_employee_management_system.py` to run unit tests and validate system functionality.



