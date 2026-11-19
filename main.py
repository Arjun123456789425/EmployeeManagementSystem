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