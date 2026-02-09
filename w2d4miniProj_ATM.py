# ATM Decision making System

# This program checks the PIN and balance in the user Bank account
# 
#  

# Assume the below value from the user DB
stored_pin = "1234"
stored_balance = 5000


#Taking the input from the user
entered_pin= input("Hello User, Enter your PIN : ")
withdraw_amount = float(input("Enter Withdrawal Amount : "))

if entered_pin == stored_pin: 
    if withdraw_amount <= stored_balance:
        print("Trasaction success :")
        print(f"Please collect your cash: {withdraw_amount}")
        print(f"Remaining balance: {stored_balance - withdraw_amount}") 
    else:
        print("Insufficient Balance : ")
else:
    print("Enter the right PIN : ")
