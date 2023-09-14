
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

class Bank:
    def __init__(self, cardDB):
        self.cardDatabase = cardDB
        self.userChoiceNumber = 0

    def userChoice(self):
        self.userChoiceNumber = int(input("What do you wanna do? 1: Deposit, 2: Withdraw, 3: Transfer, 4: Balance Check, 5: Exit"))
        if self.userChoiceNumber == 1:
            self.cashDeposit()
        elif self.userChoiceNumber == 2:
            self.cashWithdraw()
        elif self.userChoiceNumber == 4:
            self.balanceCheck()
        elif self.userChoiceNumber == 5:
            print("Exiting...")
            return -1

    def cashWithdraw(self):
        userAccountNumber = int(input("What is your Account Number: "))
        for i in self.cardDatabase:
            if(i['accountNumber'] == userAccountNumber):
                userAmount = int(input("How much do you want to withdraw: "))
                if(userAmount<=i['bankBalance']):
                    # Memory References
                    i['bankBalance']-= userAmount
                    print(f"You have successfully withdrawn ${userAmount}. Remaining Amount: ${i['bankBalance']}")
                else:
                    print ("You do not enough money to withdraw")
                    break
        return -1

    def cashDeposit(self):
        userAccountNumber = int(input("What is your Account Number: "))
        for i in self.cardDatabase:
            if(i['accountNumber'] == userAccountNumber):
                userAmount = int(input("How much money do you want to deposit: "))
                i['bankBalance']+= userAmount
                print(f"You have successfully withdrawn ${userAmount}. Remaining Amount: ${i['bankBalance']}")
            else:
                print ("Your account number does not match our database.")
                break

    def balanceCheck(self):
        userAccountNumber = int(input("What is your Account Number: "))
        for i in self.cardDatabase:
            if(i['accountNumber'] == userAccountNumber):
                print(f"Your account has ${i['bankBalance']}")
    

bankObj = Bank(cardDatabase)
bankObj.userChoice()




