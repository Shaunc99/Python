
# Create a class named DOG and create 2 attributes (attributes are just the variables of the class you create like self.name = "Ali") i.e, name and breed. The value of these attributes should be initialized when the object for this class is created. Create 2 methods bark and get_breed, bark should return a string "{self.name} says Woof!" and get_breed should return the string "{self.name} is a {self.breed}"

class Dog:
    
    # Constructor Function
    def __init__(self,name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return f"{self.name} says Woof!"
    def get_breed(self):
        return f"{self.name} is a {self.breed}"
    
dogObj = Dog("Puki", "German Shepherd")


# bank Account. Attributes: balance, transactionHistory=[{transactionId, amount, receiversAcc, senderAcc}], Methods: withdraw, deposit, transfer, checkBalance

cardDatabase = [{'accountNumber': 987, 'bankBalance': 7000},
                {'accountNumber': 981, 'bankBalance': 800},
                {'accountNumber': 487, 'bankBalance': 100},{'accountNumber': 227, 'bankBalance': 100000},{'accountNumber': 187, 'bankBalance': 6700}
                ]

# 

class Bank:
    def __init__(self, cardDB):
        self.cardDatabase = cardDB
        self.userChoiceNumber = 0

    def userChoice(self):
        self.userChoiceNumber = int(input("What do you want to do?\n1: Deposit,\n2: Withdraw,\n3: Transfer,\n4: Balance Check,\n5: Exit\n\nEnter here: "))
        if self.userChoiceNumber == 1:
            self.cashDeposit()
        elif self.userChoiceNumber == 2:
            self.cashWithdraw()
        elif self.userChoiceNumber == 4:
            self.balanceCheck()
        elif self.userChoiceNumber == 5:
            print("Exiting...")
            return -1
        else:
            print("\nYou entered the wrong input, please try again.\n")
            self.userChoice()

    def cashWithdraw(self):
        userAccountNumber = int(input("\nEnter your Account Number: "))
        # for 
        for i in range(0,len(self.cardDatabase)):
            if(self.cardDatabase[i]['accountNumber'] == userAccountNumber):
                print("The account number matched")
                userAmount = int(input("How much do you want to withdraw: "))
                if(userAmount<=self.cardDatabase[i]['bankBalance']):
                    # Memory References
                    self.cardDatabase[i]['bankBalance']-= userAmount
                    print(f"You have successfully withdrawn ${userAmount}. Remaining Amount: ${self.cardDatabase[i]['bankBalance']}")
                    break
                else:
                    print("You do not enough money to withdraw, please try again.")
                    self.cashWithdraw()
                    break

            # print(i == len(self.cardDatabase)-1)
            if (i == len(self.cardDatabase)-1):
                print("\nYour account doesn't match with our database, please try again.\n")
                self.cashWithdraw()
        return -1

    def cashDeposit(self):
        userAccountNumber = int(input("What is your Account Number: "))
        for i in range(0,len(self.cardDatabase)):
            if self.cardDatabase[i]['accountNumber'] == userAccountNumber:
                print("Your account number matches with our database, processing...")
                userAmount = int(input("How much do you want to Deposit: "))
                self.cardDatabase[i]['bankBalance'] += userAmount
                print(f"You have successfully deposited ${userAmount}. Remaining Amount: ${self.cardDatabase[i]['bankBalance']}")
                break
            # print(i == len(self.cardDatabase)-1)
            if i == len(self.cardDatabase)-1:
                print("\nYour account doesn't match with our database, please try again.\n")
                self.cashDeposit()
        return -1
    def balanceCheck(self):
        userAccountNumber = int(input("What is your Account Number: "))
        for i in range(0,len(self.cardDatabase)):
            if self.cardDatabase[i]['accountNumber'] == userAccountNumber:
                print("Your account number matches with our database, processing...")
                print(f"Your account has ${self.cardDatabase[i]['bankBalance']}")
                break
            # print(i == len(self.cardDatabase)-1)
            if i == len(self.cardDatabase)-1:
                print("\nYour account doesn't match with our database, please try again.\n")
                self.balanceCheck()
        return -1
    

bankObj = Bank(cardDatabase)
bankObj.userChoice()




