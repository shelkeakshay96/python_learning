class BankAccount:
    ROI = 10.5
    def __init__(self) -> None:
        self.name = ''
        self.amount = ''

    def display(self):
        print('Name of user :', self.name)
        print('Account balance amount :', self.amount)

    def deposite(self):
        self.name = str(input('Enter name of user : '))
        self.amount = int(input('Enter amount to deposite : '))

    def withdraw(self):
        while (True):
            withdrawAmount = int(input('Enter amount to withdraw : '))
            if (withdrawAmount > self.amount):
                print('Insufficiant Balance. Check the balance and withdraw')
            else:
                break

        self.amount = self.amount - withdrawAmount

    def calculateIntrest(self):
        intrest = self.amount * (BankAccount.ROI / 100)
        print('Intrest on amount {} is : {}'. format(self.amount, intrest))

def main():
    print('Bank Account')
    user1 = BankAccount()
    user1.deposite()
    user1.display()
    user1.withdraw()
    user1.display()
    user1.calculateIntrest()
    print('------------------')
    user2 = BankAccount()
    user2.deposite()
    user2.display()
    user2.withdraw()
    user2.display()
    user2.calculateIntrest()

if (__name__ == '__main__'):
    main()
