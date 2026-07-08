# name=input("enter the name:")
# Maths=int(input("enter  Maths marks:"))
# English=int(input("enter English marks: "))
# History=int(input("enter History marks:"))
# Marathi=int(input("enter Marathi marks:"))
# Hindi=int(input("enter Hindi marks:"))
# total=Maths+English+History+Marathi+Hindi
# percentage=(total / 500) * 100
# if percentage >= 90:
#     Grade = "A"
# elif percentage >= 80:
#     Grade = "B"
# elif percentage >= 70:
#     Grade="C"
# elif percentage >= 60:
#     Grade="D"
# else:
#     Grade="Fail"
# print("Student name:",name)
# print("Total:",total)
# print("Percentage:",percentage)
# print("Grade :",Grade)
 
Balance = 10000

while True:
    print("\n=== ATM MENU ===")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Current Balance:", Balance)

    elif choice == 2:
        amount = int(input("Enter deposit amount: "))

        if amount > 0:
            Balance += amount
            print("Deposit Successful")
            print("Updated Balance:", Balance)
        else:
            print("Invalid amount")

    elif choice == 3:
        withdraw = int(input("Enter withdrawal amount: "))

        if withdraw > 0:
            if withdraw <= Balance:
                Balance -= withdraw
                print("Withdrawal Successful")
                print("Remaining Balance:", Balance)
            else:
                print("Insufficient Balance")
        else:
            print("Invalid amount")

    elif choice == 4:
        print("Thank you for using our ATM!")
        break

    else:
        print("Invalid Choice")