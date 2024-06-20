#ipv6 valitation by reading the ip address from text file
import sys

file = open("ip_address.txt","r")
read = file.readlines()
for line in read:
    ip = line
    ip = ip.replace("\n","")
    hextets = ip.split(":")
    flag = 0 
    count = 0
    #check the heterts length is less than 
    if len(hextets) != 8:
        print(f"\n{ip} \t-\t invalid Ip address")
        sys.exit()

    #check the hextet length is less than 4
    for hextet in hextets: 
        if len(hextet) != 4: 
            flag = 1
            print(f"\n{ip} \t\t-\t invalid Ip address")
            break
        else:
            hextet = hextet.lower()  #converting hextet uppercase to lowercase
            if not hextet.isalnum(): #check the hextet is alphnumeric
                print("hextets must be mixed with alphabet and numberic character\n")
                sys.exit()
            if hextet.startswith("0"): #check the hextet startwith 0 then replace with empty string
                hextets[count] = hextet.replace("0","",1)
                if hextets[count] == "000": #check hextets contains series of and replace with ":"  
                    hextets[count] = hextets[count].replace(hextets[count],":")
            count +=1
            
            try:
                int(hextet,16)
                continue
            except ValueError:
                flag = 1
                print("\nthe hextet is out of range.The hextet should be range of 0 to 9 and a to f")
                
            
    if flag == 0:         
        print(f"\n{ip} \t-\t valid Ip address")  