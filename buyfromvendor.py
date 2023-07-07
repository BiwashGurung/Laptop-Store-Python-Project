from read import read_data
import datetime 
import os
from write import VendorBuy
from write import grandTotal


GrandTotal=0
#The process of purchasing laptops
def buy_laptops(billno):
    vendor_name=input("Enter the name of your Company : ")
    vendor_address=input("Enter the address of your Company : ")
    vendor_contact=input("Enter the contact number of your Company : ")
    if(len(vendor_name) > 0 and len(vendor_address) > 0 and len(vendor_contact) > 0): 
            Buying(vendor_name, vendor_address, vendor_contact,billno)
    else:
        os.system("cls")
        print("""
        "Kindly complete the information requested"
        """)
        input("Please hit the Enter key to go back ")
        
# This approach is for initiating the laptop purchase process and choosing a laptop 
def Buying(inputed_Name, inputed_Address, inputed_Contact,billno):
    laptops=read_data()
    print('''           "Pick a number from the options provided below" 
                        +---------------------------------------+                                       
                        |            Laptop to buy              |
                        |---------------------------------------|
                        |      [1] Razer Blade                  |
                        |      [2] XPS                          | 
                        |      [3] Alienware                    |
                        |      [4] Swift 7                      |
                        |      [5] Macbook Pro 16               |
                        +---------------------------------------+
                                                               
  ''')
    try:
        print( "Select 77: to go back to the main menu ")
        print("Select between  1-5 : To Choose a Laptop :")
        user_option = input("Enter Your choice here : ")
        for i in range(len(laptops)):
            if(int(user_option) == i+1):
                company_details(inputed_Name, inputed_Address, inputed_Contact,i,billno)
        if(user_option == "77"):
            return None
        if(user_option> str(len(laptops)) or user_option < "0" ):
                print('"Please ensure that your choice is entered correctly"')
                input("Press Enter ")
                Buying(inputed_Name, inputed_Address, inputed_Contact, billno)    
    except:
         if(user_option > str(len(laptops)) or user_option < "0" ):
            print("Please ensure that your choice is entered correctly")
            input("Press Enter ")
            Buying(inputed_Name, inputed_Address, inputed_Contact, billno)

#   "This process is designed for buying laptops and handling billing procedures"
def company_details(inputed_Name, inputed_Address, inputed_Contact, sn, billNo):
    number = int(input("Please indicate the desired quantity of laptops :"))
    if(number > 0):
        number = str(number)
        VendorBuy(inputed_Name, inputed_Address, inputed_Contact,sn,number, billNo)
        changeStock(sn,number)
        os.system("cls")
        buyAgain(inputed_Name, inputed_Address, inputed_Contact, billNo)  
    else:
        print("Temporarily unavailable for purchase")
        input("Press Enter ")
        Buying

# This process is designed for updating stock levels
def changeStock(sn,num):
    laptop_data=read_data()
    laptop_data[int(sn)][3]=int(laptop_data[int(sn)][3])+int(num)
    laptop_data[int(sn)][3]=str(laptop_data[int(sn)][3])
    file=open('laptops.txt','w')
    for i in range(len(laptop_data)):
        for j in range(len(laptop_data[i])):
            if j==5:
                file.write(laptop_data[i][j])
            else:
                 file.write(laptop_data[i][j]+',')
        file.write('\n')
    file.close()
# This process is designed for determining the overall cost"


# This approach is intended for reselling laptops
def buyAgain(company_Name, company_Address, company_Contact, billNo):
    print(f"""
            +----------------+
            |  1.Buy Again   |
            |----------------|
            |  2.End Buying  |
            +----------------+
""") 
    Option=input("Please choose between 1 and 2 : ")
    if(Option=="1"):
        Buying(company_Name, company_Address, company_Contact, billNo)
    elif(Option=="2"):
        os.system("cls")
        print("Laptops were sold successfully .....")
        grandTotal(company_Name,billNo)
        with open(company_Name+billNo+"_Bill.txt","r")as bill:
                print(bill.read())
        input("Press Enter to go back to the previous screen")
    else:
        print("Input error: please enter the required information accurately")
        print("Press Enter to go back to the previous screen")
        buyAgain(company_Name, company_Address, company_Contact, billNo)
