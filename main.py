from Contract import Contract
from Permanent import Permanent
print('Permanent Employee')
empp = Permanent('Arjun', 60000)
empp.display_details()
empp.calculate_salary()

print('Contract Employee')
cmpp = Contract('Rahul', 25000)
cmpp.display_details()
cmpp.calculate_salary()


 #   OUTPUT

# Permanent Employee
# Name: Arjun
# Salary: 60000
# Total Salary: 72000.0
# Contract Employee
# Name: Rahul
# Salary: 25000
# Total Salary: 26250.0
# ###########################################################
# Model: Benz
# Rent: 4000
# Rent of the car is: 24500
# ____________________________________________
# Model: R15
# Rent: 1500
# Rent of the Bike is : 10600