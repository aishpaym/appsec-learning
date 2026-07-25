with open("students.txt","w") as file:
     file.write("Aishwarya")
with open("students.txt","a") as file:
     file.write("\n Quality Analyst")


with open("students.txt","r") as file:
     for txt in file:
          print(txt.strip())
