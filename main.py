
def buy_airtime():
    cash = 10000
    time = "12:23pm"
    date = "12/11/2022"
    amount = int(input("Enter amount: "))
    balance = cash - amount
    print("Airtime of ",amount, "bought on ",date, "at ", time, "New balance is ", balance )

def deposit():
    cash = 1000
    amount = int(input("Enter amount: "))
    new_balance = cash + amount

    print("Amount", amount, "deposited successfully new balance is : ", new_balance)


def send_money():
    cash = 10000
    time = "12:23pm"
    date = "12/11/2022"
    receiver = int(input("Enter the number: "))
    amount = int(input("Enter amount: "))
    if amount > 0 and amount <= cash:
        new_bal = cash - amount
        print("Amount ksh", amount, "sent to ", receiver,"on ", date, "at", time, "new balance is: ", new_bal)
    else:
        print("Not enough cash is your account ")


def withdraw_cash():
    cash = 10000
    time = "12:23pm"
    date = "12/11/2022"
    Agent = int(input("Enter the agent number: "))
    amount = int(input("Enter amount: "))
    if amount> 0 and amount <= cash:
        remaining_cash = cash - amount
        print("Ksh ",amount, "withdrawn successfully from agent number ",Agent, "on", date, "at ", time, "balance is ",remaining_cash)
    else:
        print("Not enough money in your account ")

def pay_bill():
    cash = 10000
    time = "12:23pm"
    date = "12/11/2022"
    paybill = int(input("Enter the paybill no. "))
    amount = int(input("Enter amount: "))
    if amount >0 and amount<= cash:
        bal= cash - amount
        print("Ksh", amount, "paid to ", paybill, "Agencies on" ,date, "at", time, "new balance is: ", bal)
    else:
        print("Not enough money in your account ")


while True:
    print("Welcome to Impact Transfer")
    print("1. Send Money")
    print("2. Deposit Cash")
    print("3. Withdraw Money")
    print("4. But Airtime")
    print("5. Pay Bill")

    user = int(input("Choose Option: "))
    if user ==1:
        send_money()
    elif user == 2:
        deposit()
    elif user == 3:
        withdraw_cash()
    elif user == 4:
        buy_airtime()
    elif user ==5:
        pay_bill()
    else:
        print("Make a valid choice")