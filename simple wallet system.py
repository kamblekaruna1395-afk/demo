Balance = 50000

while True:
    print("\n=== Wallet Menu ===")
    print("1. Check balance")
    print("2. Add money")
    print("3. Spend money")
    print("4. Exit")

    choice = int(input("Enter the choice number: "))

    if choice == 1:
        print("Current balance:", Balance)

    elif choice == 2:
        amount = int(input("Enter amount to add: "))

        if amount > 0:
            Balance += amount
            print("Money added successfully")
            print("New balance:", Balance)
        else:
            print("Invalid amount")

    elif choice == 3:
        spend_money = int(input("Enter spend amount: "))

        if spend_money <= Balance:
            Balance -= spend_money
            print("Payment successful")
            print("Remaining balance:", Balance)
        else:
            print("Insufficient balance!!")

    elif choice == 4:
        print("Thank you for using Wallet!!")
        break

    else:
        print("Invalid Choice")
    


    