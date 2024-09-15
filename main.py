# Taks1
# class Emploe:
#     def __init__ (self,name,_salary,__id):
#         self.name = name
#         self.salary = _salary
#         self.id = __id
#     def show_info (self):
#         print(f"name:{self.name}\nsalary:{self.salary}\nid:{self.__id}")

# obj1 = Emploe("Abubakr",1500,800848412)
# obj1.show_info()
# Данный код создан.
# у нас есть атрибут 'name' который является публичной -> оно отобразится (без каких либо ошибок!)
# также имеется атрибут 'salary' который является зашишенным! В нашем коде данный атрибют отабразится вне кода (без каких либо ошибок)
# и наконец последний атрибют 'id' который является личным.В конце при запуске программы будет ошибка так как данный отрибют скрытен от постороних клаз
# solved:
# Task2
# class BankAccount:
#     def __init__(self, balance, pin):
#         self._balance = balance  # "protected" атрибут
#         self.__pin = pin  # "private" атрибут


# account = BankAccount(1000, 1234)


# print(f"Balance: {account._balance}")

# try:
#     print(f"PIN: {account.__pin}")
# except AttributeError as e:
#     print(f"Ошибка: {e}")
# in prograss
# Task3
# class BankAccount:
#     def __init__(self, initial_balance=0):
#         self._balance = initial_balance

#     @property
#     def balance(self):
#         return self._balance

#     @balance.setter
#     def balance(self, value):
#         if value < 0:
#             raise ValueError("Balance cannot be negative.")
#         self._balance = value


# account = BankAccount(100)
# print(account.balance)  

# account.balance = 200 
# print(account.balance)  

# account.balance = -50  

# solved:

# Task4

# class Animal:
#     def speak(self):
#         return "Animal speaks"

# class Dog(Animal):
#     def speak(self):
#         return "Dog barks"

# class Puppy(Dog):
#     def speak(self):
#         return "Cats meow"

# puppy = Puppy()
# print(puppy.speak())
# solved:

# Task5
# class Person:
#     def __init__ (self,name,country,dayofbirth):
#         self.name = name 
#         self.country = country
#         self.dayofbirth = dayofbirth
#     def ageofper (self):
#         print(f"name: {self.name}\ncountry: {self.country}\ndayofbirth: {self.dayofbirth} is 23 years old")

# person1 = Person("Micheal","USA",2002)
# person1.ageofper()

# solved:

# Task6
# class Nobel:
#     def __init__(self, category, year, winner):
#         self.category = category
#         self.year = year
#         self.winner = winner

#     def __str__(self):
#         return f"Nobel Prize in {self.category} ({self.year}) awarded to {self.winner}"


# np2005 = Nobel("Peace", 2005, "Muhammad Yunus")

# print(np2005)
# solved:
# Task7

# def getCase(word):
#     if word.isupper():
#         return "upper"
#     elif word.islower():
#         return "lower"
#     else:
#         return "mixed"
    
# print(getCase("whisper..."))  
# print(getCase("SHOUT!"))     
# print(getCase("Whisper"))    
# print(getCase("hellO"))   
# solved:  

# Task8
# def fibonachi (f):

# def phi(n):
#     if n == 0 or n == 1:
#         return 1
#     a, b = 1, 1
#     for _ in range(2, n + 1):
#         a, b = b, a + b
#     return b

# n = int(input())
# print(phi(n))
# solved:


# Task9:
# user_input = int(input("Enter a number: "))
# i = 1
# for i in range(i, user_input + 1):
#     if i <= user_input // 2 + 1:
#         print((str(i) + ' ') * i) 
#     else:
#         print((str(i) + ' ') * (user_input - i + 1)) 

# user_input has to be '9'
# solved:

# Task10:
class IceCream:
          def __init__(self, flavor, num_sprinkles):
              self.flavor = flavor
              self.num_sprinkles = num_sprinkles
          def sweetest_icecream (self):
                 
                 
                 
                 
       




    

     
        

  

