class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance


    def deposit(self, amount):
        self.balance += amount
        print(self.balance)
        return(self)



    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient funds: Charging a $5 fee.")
            self.balance -= 5
        else:
            self.balance -= amount
            print(self.balance)
            return(self)


    
    def display_account_info(self):
        print(self.balance)
        return(self)



    def yield_interest(self):
        sum = self.balance * self.int_rate
        print(sum)
        return(self)




bankOne = BankAccount(0.03, 100)
bankOne.deposit(10).deposit(20).deposit(100).withdraw(100).yield_interest().display_account_info()

print("--------------")

bankTwo = BankAccount(0.04, 500)
bankTwo.deposit(20).deposit(40).withdraw(50).withdraw(100).withdraw(30).withdraw(130).yield_interest().display_account_info()

