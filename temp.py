class ATM:
   def __init__(self, bank_name, balance):
    self.bank_name = bank_name
    self.balance = balance
    self.withdrawls = []
    
   def print_information(self):
      print("Welcome to %s,Your balance is %d"%( self.bank_name, self.balance) ) 

   def valid(self , request):
      if request <= 0  |  request > self.balance:
         return False
      else:
         return True

   def withdraw(self, request):
      self.print_information()
      notes=[100,50,10,5]
      if self.valid(request):
         self.withdrawls.append(request)
         self.balance -= request
         
         for note in notes:
            if request >= note:
                while request>=note:
                    print('give',str(note))
                    request -= note
            
            elif request > 0 : 
                print('give' ,str(request))
                request=0
      else:
         print("Your request is not valid")
         
   def show_withdrawls(self):
    for x in self.withdrawls:
        print(str(x))
            
atm1=ATM("barakeh",10000)
atm1.withdraw(4054)
atm1.withdraw(500)
atm1.show_withdrawls()

