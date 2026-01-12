class ATM:
    def __init__(self,pin,balance):
        self._pin = pin 
        self._balance = balance
        
    def check_balance(self,pin):
        if pin == self._pin:
            print("current balance:", self._balance)
        else:
            print("Incorrect Pin")
    
    def withdraw(self, pin , amount):
        if pin != self._pin:
            print("Incorrect PIN")
        elif amount > self._balance:
            print("Insufficient balance")
        else:
            self._balance -= amount
            print("Withdrawl successful")
            print("remaining balance:", self._balance)

atm = ATM(1234, 5000)

atm.check_balance(1234)
atm.withdraw(1234, 2000)
atm.withdraw(1234, 4000)
atm.check_balance(1111)
    
