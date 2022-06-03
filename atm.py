class Atm(object):
    def __init__(self,atmCard,pinNo):
        self.atmCard = atmCard,
        self.pinNo = pinNo
    
    def cashWithdrawal(self):
        print("Cash is withdrawed")

    def balanceEnquiry(self):
        print("You have $1500 left in your bank account")