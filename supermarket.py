print("Wellcome to my supermarket")
items = {
    "rice": 50,
    "milk": 30,
    "bread": 40,
    "egg": 10,
    "sugar": 45
}
print(items)

while True:
    choice = input("Enter item name: ")
    print("You selected:", choice)
    print("Price:", items[choice])

    more = input("Do you want add more items? yes/no: ")

    if more == "no":
        break
