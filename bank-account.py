class BankAccount:
    def __init__(self, int_rate, balance,):
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



class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        # self.account = BankAccount(int_rate=0.02, balance=0)
        self.account = {
            "bankOne" : BankAccount(.02,1000),
            "bankTwo" : BankAccount(.05,3000)
        }

    def display_user_balance(self):
        print(f"User: {self.name}, Bank One: {self.account['bankOne'].display_account_info()}")
        print(f"User: {self.name}, Bank Two: {self.account['bankTwo'].display_account_info()}")
        return self

    def make_deposit(self,amount):
        self.account += amount
        return(self)

    def make_withdraw(self,amount):
        self.account -= amount
        return(self)

print("---------")

brittany = User("brittany", "brit69@aol.com")
brittany.account['bankOne'].deposit(100)
brittany.account['bankOne'].withdraw(150)








