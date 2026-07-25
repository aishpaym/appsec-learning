with open("server_logs.txt","w") as file:
     file.write("INFO Login Successful")
     file.write("\nERROR Database Connection Failed")
     file.write("\nINFO User Logged Out")
     file.write("\nWARNING Disk Space Low")
     file.write("\nERROR API Timeout")
i=0
with open("server_logs.txt","r") as file:
     for line in file:
          if "ERROR" in line:
               print(line.strip())
               i+=1

print("The  total number of Errors: ",i)
               
