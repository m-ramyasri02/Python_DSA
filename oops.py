'''class A:
    def __init__(self,name,age,gender):
        self.name=name#private variable can be accessed only inside the class
        self.age=age#protected variable can be accessed inside the class and outside of the class but not  in the child class
        self.gender=gender#public variable can be accessed outside the class and inside of the same class
def display(self):
    print(self.__name)
    print(self._age)
    print(self.gender)
a1=A("sandhya",20,"female")
#print(a1.__name)
#print(a1.gender)
print(a1.display())'''

'''from abc import ABC,abstractmethod
class BankAccount(ABC):
    def __init__(self,balance):
        self.__balance=balance
    def deposit(self,amount):
        self.__balance+=amount
    def withdraw(self,amount):
        self.__balance-=amount
    def getbalance(self):
'''

class Animal:
    print("animal sound")
class dog(Animal):
    def sound(self):
        print("woof")
class cat(Animal):
    def sound(self):
        print("meow")
