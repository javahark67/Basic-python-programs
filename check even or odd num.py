while True:

   number =int(input("Enter number:"))
    
   if number % 2 == 0:
    print("Even")

   else:
     print("odd")

   check_another = input("Do you want to check another yes/no:")
   
   if check_another == "no":
       break
