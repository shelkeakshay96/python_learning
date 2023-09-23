class ATM:
    ROI = 9.5
    def __init__(self, atm, amount):
        self.balance = amount
        self.atm = atm
    
    def displayBalance(self):
        print('Your savings Balance from {} is : {}'. format(self.atm, self.balance))

    def withraw(self, amount):
        if (self.balance < amount):
            print('Insufficiant balance')
        else:
            self.balance = self.balance - amount
        self.displayBalance()
    
    def deposite(self, amount):
        self.balance = self.balance + amount
        print('Amount {} deposited successfully'. format(amount))
        self.displayBalance()

    @classmethod
    def displayBankInfo(cls):
        print('Rate of intrest is : {}' . format(cls.ROI))

    @staticmethod
    def displayAction():
        print('1 => Check Balance', end= '              ')
        print('2 => Withday')
        print('3 => Deposite', end= '                   ')
        print('4 => See Bank Info')
        print('5 => Switch ATM', end= '                 ')
        print('0 => Exit')

def switchATM(hdfc, icici):
    print('1 => HDFC')
    print('2 => ICICI')

    atm = int(input('Choose atm of bank : '))
    while (True):
        if(atm == 1):
            bank = hdfc
            break
        elif (atm == 2):
            bank = icici
            break
        else:
            print('invalid atm')

    return bank

def main():

    hdfc = ATM('HDFC', 3000)
    icici = ATM('ICICI', 10000)

    print('1 => HDFC')
    print('2 => ICICI')
    bank = int(input('Choose atm of bank : '))
    while (True):
        if (bank == 1):
            atmOfBank = hdfc
            break
        elif (bank == 2):
            atmOfBank = icici
            break
        else:
            print('invalid atm')

    ATM.displayAction()

    while (True):
        no = int(input('Enter your action : '))
        if (no == 1):
            atmOfBank.displayBalance()
        elif (no == 2):
            no = int(input('Enter amount to withdraw : '))
            atmOfBank.withraw(no)
        elif (no == 3):
            no = int(input('Enter amount to Deposite : '))
            atmOfBank.deposite(no)
        elif (no == 4):
            ATM.displayBankInfo()
        elif (no == 5):
            atmOfBank = switchATM(hdfc, icici)
            ATM.displayAction()
        elif (no == 6):
            break
        else:
            print ('--Invalid input--')
            ATM.displayAction()
if (__name__ == '__main__'):
    main()
