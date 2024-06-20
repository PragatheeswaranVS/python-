print("---------------------------------------")
print("                  MENU                 ")
print("---------------------------------------")
print("vadai = 30")
print("soda = 20")
print("sandwich = 100")
print('----------------------------------------')
vadai_cost = 30
soda_cost = 20
sandwich_cost = 100
vadai_quantity = int(input("how many vadai you want :")) 
soda_quantity = int(input("how many soda you want :"))
sandwich_quantity = int(input("how many sandwich you want :"))
'''
print(vadai_quantity)
print(soda_quantity)
print(sandwich_quantity)
'''
total_amount = float(vadai_cost * vadai_quantity) + (soda_cost * soda_quantity) + (sandwich_cost * sandwich_quantity)
print("the amount you need to pay : ",total_amount)
received_amount = float(input("amount you paid :"))
balance_amount = received_amount - total_amount
print("the received amount :",received_amount)
print("collect the balance amount :",balance_amount)