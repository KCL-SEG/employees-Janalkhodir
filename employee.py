"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class HourlyContract:

    def __init__(self, hourly_pay, hours):
        self.hourly_pay = hourly_pay
        self.hours = hours

    def get_pay(self):
        return self.hourly_pay * self.hours

    def __str__(self):
        string = f'contract of {self.hours} hours at {self.hourly_pay} per hpur'
        return string

class SalaryContract:

    def __init__(self, salary):
        self.salary = salary

    def get_pay(self):
        return self.salary

    def __str__(self):
        string = f' monthly salary of {self.salary}'
        return string

class BonusCommission:

    def __init__(self, bonus):
        self.bonus = bonus

    def get_pay(self):
        return self.bonus 

    def __str__(self):
        string = f'bonus commission of {self.bonus}'
        return string

class ContractCommission:

    def __init__(self, contracts=0, commission=200):
        self.contracts = contracts
        self.commission = commission

    def get_pay(self):
        return self.contracts * self.commission


    def __str__(self):
        string = f'Commissin for {self.contracts} contract at {self.commission} commission'
        return string



class Employee:
    def __init__(self, name, contract, commission=None):
        self.name = name
        self.contract = contract
        self.commission = commission

    def get_pay(self):
        pay = self.contract.get_pay()
        if self.commission:
            pay += self.commission.get_pay()
        return pay

    def __str__(self):
        string = f'{self.name} works on {str(self.contract)}'
        if self.commission:
            string += f'and get {str(self.commission)}'
        string += f' The toatal pay is {self.get_pay()}'
        return string


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie')

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie')

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee')

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan')

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie')

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel')
