import csv

class Employee:
    def __init__(self, emp_id, basic_salary, tax, travel_allowance, bonus, others):
        self.id = self.validate_int(emp_id, 'Employee ID')
        self.basic_salary = self.validate_float(basic_salary, 'Basic Salary')
        self.tax = self.validate_tax(self.validate_float(tax, 'Tax'))
        self.travel_allowance = self.validate_float(travel_allowance, 'Travel Allowance')
        self.bonus = self.validate_float(bonus, 'Bonus')
        self.others = self.validate_float(others, 'Others')
        self.gross_salary = 0
        self.net_salary = 0
        self.valid = self.compute_salaries()

    def validate_int(self, value, field_name):
        if value.strip() == '':  # Check for missing value
            print(f"Missing value for {field_name}. Defaulting to 0.")
            return 0
        try:
            return int(value)
        except ValueError:
            raise ValueError(f"Datatype mismatch detected: {field_name} should be an integer, but got '{value}'.")

    def validate_float(self, value, field_name):
        if value.strip() == '':  # Check for missing value
            print(f"Missing value for {field_name}. Defaulting to 0.")
            return 0.0
        try:
            return float(value)
        except ValueError:
            raise ValueError(f"Datatype mismatch detected: {field_name} should be a float, but got '{value}'.")

    def validate_tax(self, tax):
        if tax < 0:
            print(f"Warning: Negative tax value detected for Employee ID {self.id}. Tax has been set to 0.")
            return 0
        return tax

    def compute_salaries(self):
        if self.basic_salary <= 0:
            print(f"Skipping Employee ID {self.id} due to invalid Basic Salary ({self.basic_salary}).")
            return False
        self.gross_salary = (self.basic_salary + self.travel_allowance +
                             self.bonus + self.others)
        self.net_salary = self.gross_salary - self.tax
        return True

def find_min_max_salaries(employees):
    min_salary_emp = max_salary_emp = None
    
    for emp in employees:
        if not emp.valid:
            continue
        if min_salary_emp is None or emp.net_salary < min_salary_emp.net_salary:
            min_salary_emp = emp
        if max_salary_emp is None or emp.net_salary > max_salary_emp.net_salary:
            max_salary_emp = emp
    
    return min_salary_emp, max_salary_emp

def divide_and_conquer(employees, start, end):
    if start == end:
        return employees[start], employees[start]
    
    mid = (start + end) // 2
    left_min, left_max = divide_and_conquer(employees, start, mid)
    right_min, right_max = divide_and_conquer(employees, mid + 1, end)
    
    min_salary_emp, max_salary_emp = find_min_max_salaries([left_min, left_max, right_min, right_max])
    
    return min_salary_emp, max_salary_emp

def main():
    employees = []
    file_path = 'employees_data_missingall.csv'
    
    try:
        # Read CSV file
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    emp = Employee(
                        emp_id=row['Employee ID'],
                        basic_salary=row['Basic Salary'],
                        tax=row['Tax'],
                        travel_allowance=row['Travel Allowance'],
                        bonus=row['Bonus'],
                        others=row['Others']
                    )
                    employees.append(emp)
                except ValueError as e:
                    print(f"Skipping row due to error: {e}")
        
        if not employees:
            print("No valid employee data found.")
            return
        
        # Apply Divide and Conquer
        min_salary_emp, max_salary_emp = divide_and_conquer(employees, 0, len(employees) - 1)
        
        # Output results
        if min_salary_emp and max_salary_emp:
            print(f"Employee with Minimum Net Salary:\nID: {min_salary_emp.id}, Net Salary: {min_salary_emp.net_salary}")
            print(f"Employee with Maximum Net Salary:\nID: {max_salary_emp.id}, Net Salary: {max_salary_emp.net_salary}")
        else:
            print("No valid employees with positive basic salary found.")
    
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
