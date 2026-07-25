#Write in File
with open("notes.txt","w") as file:
     file.write("Learning Python File Handling")

#Append in the File
with open("notes.txt","a") as file:
     file.write("\nCyber Security")

with open("notes.txt","a") as file:
     file.write("\n New Text To Check")

#Read the file
file = open("notes.txt","r")
content = file.read()
print(content)
file.close()

# To Read Line by Line
file=open("notes.txt","r")
for line in file:
     print(line)
file.close()

#Using with Open--> This is preffered method becuase it automatically closes the file
with open("notes.txt","r") as file:
     content=file.read()

print(content)

#Read every line into a list
with open("fruits.txt","w") as file:
     file.write("Apple")

with open("fruits.txt","a") as file:
     file.write("\nOrange")
     
with open("fruits.txt","a") as file:
     file.write("\nBanana")
with open("fruits.txt","r") as file:
     fruits=file.readlines()
print(fruits)


#Remove Extra Newlines
with open("fruits.txt","r") as file:
     for line in file:
          print(line.strip())

import os
if os.path.exists("text.txt"):
     print("file found")
else:
     print("No file found")
