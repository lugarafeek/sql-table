class bank:
    def __init__(self,customer_name,account_number,balance):
        self.customer_name=customer_name
        self.account_number=account_number
        self.balance=balance
    
    def deposite(self,balance):
        if balance>0:
            self.balance+=balance
            print(f"deposite{balance}.new balance is{balance}")
        else:
            print("deposite amount must be positive.")   
    def withdraw(self,balance):
        if balance <= self.balance:
            self.balance-=balance
            print(f"withdraw{balance}.new balance is{balance}")
        else:
            print("no amount to withdraw")       
    def check_balance(self):
        print(f"available balance is{balance}")
customer_name=input("enter the name:")
account_number=int(input("enter the account number:"))
balance=float(input("enter the balance amount:"))

obj=bank(customer_name, account_number, balance)
obj.check_balance()
obj.deposite(10000)
obj.withdraw(5000)
obj.check_balance()







