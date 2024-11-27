#n= input("What is your dream vacation ?")
def menu():
    print("---------MENU---------")
    print("1- Where do you  want to go?")
    print("2. Pricing")
    print("3. Accomodation")
    print("4. Air Tikets or Transportation")

while True:
    menu()
    n=input("Enter a chice of what you'd like to know: ")
    if n=='1':
        print("Your dream destination is beautiful.")
    elif n=='2':
        print("The pricing is fair,food is quite cheap,accomodation can be easily found")
    elif n =='3':
        print("There are many hotels found in the area")
    elif n=='4':
        print("The air flight tickets are quite pricy but dependent on what you're flying")

