class BankAcount:
    def __init__(self,account_name):
        self.account_name = account_name
        self.balance =0

    def deposit(self,money): 
        self.balance += money
        return f"your balance is{self.balance}"
    def withdraw(self,money):
        if self.balance >= money:
            self.balance-= money
            return f'your balance is {self.balance}'
        else:
            return 'insuficient funds'    
            
    acount_name=["john","joyce"]
    airtel_money=BankAcount
    
    ("john")   
    deposit_amount= int(input("enter your amount:"))  
    print(airtel_money.deposit_amount(amount)) 
    withdraw_amount=int(input("enter your amount")) 
    print(airtel_money).withdraw_amount("enter your amount:")

                
          
