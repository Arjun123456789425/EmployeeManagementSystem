from Employee import Employee # import from parent class 

class Contract(Employee):  # Contract inherits from the Employee class
    def calculate_salary(self):
        # Apply a 5% contract allowance 1.05x multiplier via the property
        total = self.retrieve_salary * 1.05
        print('Total Salary:', total)
        return total
