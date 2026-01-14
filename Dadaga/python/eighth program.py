#Oops Concept(Abstraction and Encapsulation)
"""class Student:
    print("Adding Student Detail....")
    def __init__(self,fullname,marks):
        self.name = fullname
        self.mark = marks
        #print("Adding Student Detail....")

s1 = Student("Karan",90)
print(s1.name,s1.mark)

s2 = Student("Jigar",95)
print(s2.name,s2.mark)

class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Hi,",self.name,"your Avg. score is",sum/3)
s1 = Student("Vaibhav", [90,80,70] )
s1.avg()

s1.name = "Vikas"
s1.avg()"""

class Account :
    
    def __init__(self, bal, a_no):
        self.bal = bal
        self.a_no = a_no

    def credit(self, balance):
        self.bal += balance
        print("Rs.", balance, "is credited in your account")
        print("Total Balance is : ", self.get_balance())

    def debit(self, balance):
        self.bal -= balance
        print("Rs.", balance, "is debited in your account")
        print("Total Balance is : ", self.get_balance())
    
    def get_balance(self):
        return self.bal


a_no1 = Account(100000, "SB0123")
print("Account No : " ,a_no1.a_no)
a_no1.credit(115000)
a_no1.debit(10000)
print("Account total Balance : " ,a_no1.bal)
        

