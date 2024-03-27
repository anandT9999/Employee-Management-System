import json

class Employee:
    def __init__(self, name, emp_id, title, department):
        self.name = name
        self.emp_id = emp_id
        self.title = title
        self.department = department

    def display_details(self):
        print("Name:", self.name)
        print("Employee ID:", self.emp_id)
        print("Title:", self.title)
        print("Department:", self.department)

    def __str__(self):
        return f"{self.name} - ID: {self.emp_id}"

class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def remove_employee(self, emp_id):
        for employee in self.employees:
            if employee.emp_id == emp_id:
                self.employees.remove(employee)
                return True
        return False

    def list_employees(self):
        print(f"Employees in {self.name} department:")
        for employee in self.employees:
            print(employee)

class Company:
    def __init__(self):
        self.departments = {}

    def add_department(self, department_name):
        if department_name not in self.departments:
            self.departments[department_name] = Department(department_name)
            print(f"Department '{department_name}' added.")
        else:
            print("Department already exists.")

    def remove_department(self, department_name):
        if department_name in self.departments:
            del self.departments[department_name]
            print(f"Department '{department_name}' removed.")
        else:
            print("Department does not exist.")

    def display_departments(self):
        print("Departments:")
        for department in self.departments.values():
            print(department.name)

    def save_data(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.departments, file, default=lambda obj: obj.__dict__, indent=4)
        print("Data saved successfully.")

    def load_data(self, filename):
        try:
            with open(filename, 'r') as file:
                self.departments = json.load(file)
            print("Data loaded successfully.")
        except FileNotFoundError:
            print("File not found.")
        except json.JSONDecodeError:
            print("Error decoding JSON data.")

def print_menu():
    print("\nEmployee Management System Menu:")
    print("1. Add Department")
    print("2. Remove Department")
    print("3. Add Employee")
    print("4. Remove Employee")
    print("5. List Employees in Department")
    print("6. Display Departments")
    print("7. Save Data")
    print("8. Load Data")
    print("9. Exit")

def main():
    company = Company()
    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            department_name = input("Enter department name: ")
            company.add_department(department_name)
        elif choice == '2':
            department_name = input("Enter department name: ")
            company.remove_department(department_name)
        elif choice == '3':
            name = input("Enter employee name: ")
            emp_id = input("Enter employee ID: ")
            title = input("Enter employee title: ")
            department = input("Enter department: ")
            if department not in company.departments:
                print("Department does not exist.")
            else:
                employee = Employee(name, emp_id, title, department)
                company.departments[department].add_employee(employee)
        elif choice == '4':
            department_name = input("Enter department name: ")
            if department_name in company.departments:
                emp_id = input("Enter employee ID: ")
                removed = company.departments[department_name].remove_employee(emp_id)
                if removed:
                    print("Employee removed successfully.")
                else:
                    print("Employee not found in this department.")
            else:
                print("Department does not exist.")
        elif choice == '5':
            department_name = input("Enter department name: ")
            if department_name in company.departments:
                company.departments[department_name].list_employees()
            else:
                print("Department does not exist.")
        elif choice == '6':
            company.display_departments()
        elif choice == '7':
            filename = input("Enter filename to save data: ")
            company.save_data(filename)
        elif choice == '8':
            filename = input("Enter filename to load data: ")
            company.load_data(filename)
        elif choice == '9':
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 9.")

if __name__ == "__main__":
    main()
