menu = {
    "starter":{"*chilli chicken":90,
               "chicken 65":50,
               "~pepper chicken":80,
               "paneer 65":50},
    "main dish":{"chicken biryani":120,
                 "mutton biryani":150,
                 "plain biryani":90,
                 "zeera biryani":100},
    "dessert":{"ice cream":30,
               "gulab jamun":50,
               "apple cake":50,
               "rasgulla":60}
}
print("welcome to HOTEL TAJ")
print("if you want to see the menu enter \"1\"\nif you want to add new dish Enter \"2\"")
# print the menu
def printmenu():
    print("\nNOTE:\t\"*\" - Too spicy\n\t\"~\" - Less spicy")
    for key,value in menu.items():
        varity = key.title()
        print(f"\n{varity}")
        for item,price in value.items():
            food = item.title()
            rate = price
            print(f"\t{food}\t-\tRS.{rate}/-")
            
choice = int(input("enter your choice: "))
if choice == 1:
    printmenu()
elif choice == 2:
    print("In which varity you want to add a new item .for example:(starter,main course,dessert)")
    print("If you want to add item in starter .Enter \"1\"\nIf you want to add item in main course .Enter \"2\"\nIf you want to add item in dessert .Enter \"3\"")
    choice = int(input("enter your choice: "))
    if choice == 1:
        need =int(input("How many item you want to add: "))
        if need > 0:
            for i in range(need):
                food = input(f"enter the food {i+1} name: ")
                rate = input(f"enter the rate of {food}: ")
                for key in menu["starter"].keys():
                    if food in key:
                        print(f"{food} already present in menu card")
                menu["starter"][food] = rate
            print("If you want to see the menu after you added new item .Enter \"0\"")
            choice = int(input("enter your choice: "))
        else:
            print("you entered invalid number")
        if choice == 0:
            printmenu()
    elif choice == 2:
        need =int(input("How many item you want to add: "))
        if need > 0:
            for i in range(need):
                food = input(f"enter the food {i+1} name: ")
                rate = input(f"enter the rate of {food}: ")
                for key in menu["main dish"].keys():
                    if food in key:
                        print(f"{food} already present in menu card")
                menu["main dish"][food] = rate
            print("If you want to see the menu after you added new item .Enter \"0\"")
            choice = int(input("enter your choice: "))
        else:
            print("you entered invalid number")
        if choice == 0:
            printmenu()        
    elif choice == 3:
        need =int(input("How many item you want to add: "))
        if need > 0:
            for i in range(need):
                food = input(f"enter the food {i+1} name: ")
                rate = input(f"enter the rate of {food}: ")
                for key in menu["dessert"].keys():
                    if food in key:
                        print(f"{food} already present in menu card")
                menu["dessert"][food] = rate   
            print("If you want to see the menu after you added new item .Enter \"0\"")
            choice = int(input("enter your choice: ")) 
        else:
            print("you entered invalid number")
        if choice == 0:
            printmenu()     
else:
    print("Invalid choice")