class Bank:
    bank_name="SBI"
    min=3000
    def acc_creation(self,name,acc_nm):
        self.name=name
        self.acc_nm=acc_nm
        self.min=3000
        self.ba
        print("account creation")

    def printa(self,balance):
        self.balance=balance
        print("balance is")

    def printa(self,deposit):
        self.deposit=deposit
        print("minimum balance is",self.min_blnce)
        print("amount withdrawn",self.deposit-self.min_blnce)
        print("deposited amount",self.deposit)
        print(Bank.bank_name)
ob=Bank()
ob.printa(50000)