num1= float(input("Enter the 1st Number"))
num2= float(input("Enter the 2nd Number"))
print("Choose operation")
print("1.Add +")
print("2.sub -")
print("Multiply *")
print("Divide /")

choice =input("Enter the choice (1/2/3/4)")
if choice == "1":
 print("Result =", num1 + num2)
elif choice == "2":
 print("Result =", num1 - num2)
elif choice == "3":
 print("Result =", num1 * num2)
elif choice == "4":
 if num2 !=0:
    print("Result=", num1 / num2 )
 else :
     print("Cannot divide by Zero")


