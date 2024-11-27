"""number = int(input("enter numner of your choice: "))
if number > 0:
    print("positive number")
elif number == 0:
    print("zero")
elif number<0:
    print("negative number")

animals=["dog","dog","dog","dog","dog"]
for animal in animals:
    print(animal.upper())

for i in range(10,0,-1):
    print(i)"""

n= int(input("Enter the number:"))
factorial=1
i=1
while i<=n:
    factorial*=i
    i+=1
print(factorial)

n= int(input("Enter number: "))
factorial =1
for i in range(1,n+1):
    factorial*=i
    print(factorial)