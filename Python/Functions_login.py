def login(username,password):
     if username=="admin" and password=="pass@123":
          return "Login Successful"
     else:
          return "Please enter the correct details"

username=input("Enter the correct username : ")
password=input("Enter the correct password: ")
print(login(username,password))
