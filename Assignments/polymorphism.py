# Use polymorphism in two child classes

class Bills: # create parent class 
    name = 'Unknown'
    total = 2000
    pay_cardnum = '1234-5678-9876-0099'

    def Pay(self): # create method for parent class
        entry_bill = input("Enter bill name: ")
        pay_bill_card = input("Enter card number: ")
        if (entry_bill == self.name and pay_bill_card == pay_cardnum):
            print("You may pay your bill")
        else:
            print("The correct amount for this bill was not entered.")


class Rent: # create child class
    due_to = 'Management'
    date_due = '03/01/2021'
    pay_checknum = 123456768987

    def Pay(self): # same method from parent class
        entry_bill = input("Enter bill name: ")
        pay_bill_check = input("Enter Account Number: ") # must pay with check instead of card
        if (entry_bill == self.name and pay_bill_check == pay_checknum):
            print("You may pay your bill")
        else:
            print("The correct amount for this bill was not entered.")

class Credit_Card: # create another child class
    bank_due = 'us bank'
    card_type = 'visa'
    pay_cash = 200  

    def Pay(self): # same method from parent class
        entry_bill = input("Enter bill name: ")
        pay_bill_cash = input("Enter Total to Be Paid: ") # must pay with cash instead of card/check
        if (entry_bill == self.name and pay_bill_cash == pay_cash):
            print("You may pay your bill")
        else:
            print("The correct amount for this bill was not entered.")

# invoke payment methods in each class

bill = Bills()
bill.Pay()

rent = Rent()
rent.Pay()

cc = Credit_Card()
cc.Pay()
        
    

    

    
