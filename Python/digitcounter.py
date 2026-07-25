password=input("Enter Password : ")

digit = 0

for char in password:
     if char.isdigit():
          digit += 1

print ("Number of digits in password is ", digit)
     
