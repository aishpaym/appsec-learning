correct_password = "Password@123"

for i in range (3):
     password=input("Enter the correct password ? ")

     if password == correct_password :
          print("Login Successful")

          break;

else :
     print("Account Locked")
     
