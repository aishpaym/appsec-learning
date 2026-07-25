#Read an IP Log file

with open("IPCheck.txt","w") as file:
     file.write("192.168.1.10")

with open("IPCheck.txt","a") as file:
     file.write("\n192.168.1.10")

with open("IPCheck.txt","a") as file:
     file.write("\n172.16.1.100")

#To read

with open("IPCheck.txt","r") as file:
     for ip in file:
          print("Scanning : ",ip.strip())
     
