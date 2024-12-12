#BANK WITHDRAWALS
def withdraw_money(current_balance, amount):
    if (current_balance >= amount):
        current_balance = current_balance - amount 
        return current_balance #return value 

balance = withdraw_money(100, 80) #balance = 100 - 80 

if (balance <= 50): #if-else statement to ensure sufficient balance 
    print("We need to make a deposit")
else:
    print("Nothing to see here!")
