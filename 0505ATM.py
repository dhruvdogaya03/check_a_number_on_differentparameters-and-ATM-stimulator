#ATM Simulator
print(":::::::::::INSERT YOUR CARD:::::::::::::::")
print(".........WELCOME PLEASE ENTER THE PIN...........")
balance=10000
pin=95758
attempts=0
while attempts<3:
    enterpin=int(input("Enter the pin :"))
    if enterpin==pin:
        print("Pin matched successfullly")
        break
    else:
        attempts+=1
        print("Wrong pin...Please try again")
else:
    
    print("To Many Attempts Please try after 24 hours")
    print("Exit")
    exit()

print("...........  WELCOME TO SBI ATM.............")
while True:
    print("1.Check balance" )
    print("2.Credit Amount")
    print("3.Deposit Amount")
    print("4.Exit")
    print("")
    choice=int(input("Enter the choice :: "))
    match choice:
        case 1:
            print("Your Account Balance = ",balance)
        case 2:
            amtocre=int(input("Enter the Amount that you want to Credit in your Bank Account :"))
            balance=balance+amtocre
            print("Money Credited Succesfully")
            print("Total Balance = ",balance)
        case 3:
            actodep=int(input("Enter the Amount that you want to deposite  "))
            if balance<actodep:
                print("Insfuccient Funds ...")
            else:
                balance=balance-actodep
                print("Amount ",actodep,"has been dopsited seccessfully.....")
                print("TOtal Balance = ",balance)
        case 4:
            print("Tap to exit ")
            break 
 