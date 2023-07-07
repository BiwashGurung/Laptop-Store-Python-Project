from operation import display
from read import read_data
import datetime
import os
import write

def sell():
    cust_name=input("Kindly provide the full name of the purchaser :")
    contact_no=input("Kindly input the purchaser's phone number :")
    cust_address=input("Kindly input the purchaser's present residence address :")

    if(len(cust_name)>0 and len(contact_no)>0 and len(cust_address)>0):
        start(cust_name,contact_no,cust_address)
    else:
        print("Kindly provide all necessary information")


        input("Press Enter to go back to the previous screen")

def details(cust_name,cust_address,cust_contact,ID):
    data=read_data()
    quantity=input("Kindly specify the desired number of laptops:")
    if((int(data[int(ID)][3])-int(quantity))>=0 and int(quantity)>0):
        write.salesBill(cust_name,cust_address,cust_contact,ID,quantity)
        update(ID,quantity)
        again(cust_name,cust_address,cust_contact)

    else:
        print("Temporarily unavailable for purchase")
        input("Hit the Enter button")
        start

def start(cust_name,cust_address,cust_contact):
    data=read_data()

    display()
    try:
        print("Kindly enter 99 to go back to the main menu")
        print( "Kindly input the ID number from 1 to 5 to choose your desired option")
        option=input("Please choose your preferred choice :")


        for i in range(len(data)):
            if(int(option)==i+1):
                details(cust_name,cust_address,cust_contact,i)
            if(option=="99"):
                return None
            if(option>str(len(data))or option<"0"):
                print("Kindly select the option that you desire")

                input("Hit the Enter button")
                start(cust_name,cust_address,cust_contact)
    except:
        if(option >str(len(data))or option<"0"):
            print("Kindly select the option that you desire")
            input("Hit the Enter button")
            start(cust_name,cust_address,cust_contact) 

def update(ID,quantity):
    data=read_data()
    data[int(ID)][3]=int(data[int(ID)][3])-int(quantity)
    data[int(ID)][3]=str(data[int(ID)][3])
    file=open("laptops.txt","w")
    for i in range(len(data)):
        for j in range(len(data[i])):
            if j==5:
                file.write(data[i][j])
            else:
                file.write(data[i][j]+",")
        file.write("\n")
    file.close()

def again(cust_name,cust_address,cust_contact):
    print(f"""
+-----------------------+
|Enter 1 to buy again   |       
+-----------------------+
+-----------------------+
|Enter 2 to stop buying |     
+-----------------------+ 
    """)
    option=input("Kindly select either option 1 or 2 :")
    if(option=="1"):
        start(cust_name,cust_address,cust_contact)
    elif(option=="2"):
        print("Your purchase has been processed successfully")
        write.final_Amount(cust_name)
        with open(cust_name + "-bill.txt","r")as bill:
            print(bill.read())
        input("Hit the Enter key to go back")
    else:
        print("You are requested to enter properly!!")
        print("Hit the Enter key to go back")
        again(cust_name,cust_address,cust_contact)







