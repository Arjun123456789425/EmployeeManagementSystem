from abc import ABC, abstractmethod

class Employee(ABC):  # Abstract base class
    def __init__(self, employee_name, salary):
        self.employee_name = employee_name  # Public attribute for the employee's name
        self.__salary = salary  # Private attribute to protect the base salary 

    @property  # Getter property to safely read the private salary attribute
    def retrieve_salary(self):
        return self.__salary

    @abstractmethod  # Abstract method: every subclass must implement this
    def calculate_salary(self):
        pass

    def display_details(self):  # method shared by subclasses to print basic employee details
        print('Name:', self.employee_name)
        print('Salary:', self.__salary)