class BankAccount:
    def __init__(self,account_number,owner,balance):
        self.account_number = account_number
        self.owner = owner 
        self.balance = balance 

    #,account_number?
    #存款 
    def deposit(self,amount ):
        self.balance += amount 
        print(f"存款{amount}元成功")  

    #提款
    def withdraw(self,amount):
        if self.balance >= amount :
            self.balance -= amount 
            print(f"提款{amount}元成功")
        else:
            print("餘額不足")

    #呼叫
    def display_balance(self):
        print(f"account_number = {self.account_number}\nowner = {self.owner}\nbalance = {self.balance}")

    
def main ():
    #account1 
    bankAccount1 = BankAccount(1,"Tom" ,30000)
    bankAccount1.display_balance()

    bankAccount1.deposit(9000)
    bankAccount1.display_balance()

    bankAccount1.withdraw(70)
    bankAccount1.display_balance()

    #account2
    bankAccount1 = BankAccount(9023,"Josh" ,2300)
    bankAccount1.display_balance()

    bankAccount1.deposit(9)
    bankAccount1.display_balance()

    bankAccount1.withdraw(7022222)
    bankAccount1.display_balance()


if __name__ == "__main__":
    main()