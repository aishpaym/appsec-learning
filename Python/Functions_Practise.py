def welcome():
     print("Welcome!, Hello World!")
welcome()



def greet(name):
     print("Hello", name , "!")

name="Aishwarya"
greet(name)


def employee(name,role):
     print("Hello ",name,"you are ",role)

name="Aishwarya"
role="QA Engineer"

employee(name,role)

def add(a,b):
     return a+b

a=10
b=5
result=add(a,b)
print(result)

def even_odd(num):
     if num%2==0:
          return "Even"
     else:
          return "Odd"

num = int(input("Enter the value to check? "))
result=even_odd(num)
print(result)


def password_checker(password):
     if len(password)>=8:
          return "Strong Password"
     else:
          return "Weak Password"

check=input("Enter the password to check? ")
print(password_checker(check))

