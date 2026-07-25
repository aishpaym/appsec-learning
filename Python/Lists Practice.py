fruits=["Apple","Mango","Pomogranate"]
print(fruits[0])
print(fruits[-1])
fruits.append("Orange")
print(fruits)

fruits.insert(1,"Banana")
print(fruits)

fruits.remove("Apple")
print(fruits)

numbers=[10,20,30]
numbers.pop(1)
print(numbers)
print(len(numbers))

colors = ["Red", "Brown", "Yellow"]

for color in colors:
     print(color)

if "Red" in colors:
     print("Found")

numbers=[10,78,90,30]
numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)

#Tuple
ports =(80,456,200)
print(ports)

print(ports[2])

#Sets
ips={"10.1.1","10.1.2","10.1.1"}
print(ips)

ips.add("10.1.3")
print(ips)

ips.remove("10.1.2")

print(ips)
