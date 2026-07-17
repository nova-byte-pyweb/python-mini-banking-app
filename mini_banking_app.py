balance = 1000
amounts = []

menu = {
    1: "Check Balance",
    2: "Deposit",
    3: "Withdraw",
    0: "Exit"
}

def access_personal_account(balance, amounts, choice):
    if choice == 1:
        print("Current balance:", balance)

    elif choice == 2:
        deposit = int(input("Deposit amount: "))

        if deposit <= 0:
            print("Please enter a valid amount.")
        else:
            balance += deposit
            amounts.append(deposit)
            print("Deposit successful.")
            print("Current balance:", balance)

    elif choice == 3:
        withdraw = int(input("Withdraw amount: "))

        if withdraw <= 0:
            print("Please enter a valid amount.")

        elif withdraw > balance:
            print("Insufficient Funds")

        else:
            balance -= withdraw
            print("Withdrawal successful.")
            print("Current balance:", balance)

    else:
        print("Invalid choice.")

    return balance


while True:
    print("\nBanking App")

    for key, value in menu.items():
        print(f"{key}. {value}")

    choice = int(input("Choose task: "))

    if choice == 0:
        print("Bank App Stopped")
        break

    balance = access_personal_account(balance, amounts, choice)