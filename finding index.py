items=input("Please enter element spearted by space:").split()
value =input("Enter element to find it'S Index:")

found = False

for i in range (len(items)):
    if items[i]==value:
        print("Index is :",i)
        found = True
        break

    if found == False:
      print("Invaild index")

     
