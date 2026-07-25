with open("numbers.txt", "w") as file:
     file.write("10")
with open("numbers.txt","a") as file:
     file.write("\n20")
     file.write("\n30")
     file.write("\n40")
     file.write("\n20")

with open("numbers.txt","r") as file:
     for num in file:
          print(num.strip())

     
     
