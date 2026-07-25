i=0
movies=[]
while i<3:
     movie=input("Enter your favourite movie")
     movies.append(movie)
     i=i+1
with open("Movies.txt","w") as file:
     for mov in movies:
          file.write(mov+"\n")
with open("Movies.txt","r") as file:
     for line in file:
          print(line.strip())
     
