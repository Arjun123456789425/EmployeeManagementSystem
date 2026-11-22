from Employee import Employee #import from parent class

class Permanent(Employee):  # Permanent inherits from the Employee class
    def calculate_salary(self):
        # Apply a 20% allowance 1.2x multiplier to the base salary via the property
        total = self.retrieve_salary * 1.2
        print('Total Salary:', total)
        return total