import read
import datetime
import os
final_amount = 0
def salesBill(cust_name,cust_address,cust_contact,ID,quantity):

    data=read.read_data()
    date_time=datetime.datetime.now()
    amount=data[int(ID)][2].replace("$","")
    total_cost=float(amount)*int(quantity)
    shipping_cost="15%"
    cost_after_shipping=total_cost+(total_cost*0.15)
    global final_amount
    final_amount+=cost_after_shipping
    if(os.path.exists(cust_name+"-bill.txt")):
        with open(cust_name +"-bill.txt","a") as file:
            file.write(f"""
 
+---------------------------------------------------+ 
      Laptop Name={data[int(ID)][0]}                             
|---------------------------------------------------| 
      Brand={data[int(ID)][1]}                                   
|---------------------------------------------------| 
      Price={data[int(ID)][2]}                                      
|---------------------------------------------------|
      Quantity={quantity}                                       
|---------------------------------------------------| 
     Shipping Cost={shipping_cost}                                
|---------------------------------------------------| 
     Total Cost (without shipping cost)=${total_cost}  
|---------------------------------------------------|
     Total Cost=${cost_after_shipping}                               
+---------------------------------------------------+ 
            """)
    else:
        with open(cust_name + "-bill.txt","w") as file:
            
            file.write(f"""
+--------------------------------------------------+            
      Buyer Name = {cust_name}                             
      Buyer Contact = {cust_address}                   
      Buyer Address = {cust_contact}                   
      Selling Date and Time ={date_time.strftime("%d-%m-%Y")}
+---------------------------------------------------+ 
      Laptop Name={data[int(ID)][0]}                             
|---------------------------------------------------| 
      Brand={data[int(ID)][1]}                                   
|---------------------------------------------------| 
      Price={data[int(ID)][2]}                                      
|---------------------------------------------------|
      Quantity={quantity}                                       
|---------------------------------------------------| 
     Shipping Cost={shipping_cost}                                
|---------------------------------------------------| 
     Total Cost (without shipping cost)=${total_cost}  
|---------------------------------------------------|
     Total Cost=${cost_after_shipping}                               
+---------------------------------------------------+    
""")
            


def final_Amount(cust_name):
    global final_amount
    with open(cust_name + "-bill.txt","a") as file :
        file.write(f"""
+-------------------------------+ 
 Final Amount = {final_amount}  
+-------------------------------+ 

        """)
final_amount=0









def VendorBuy(inputed_Name, inputed_Address, inputed_Contact,sn,num, billNo):
    data=read.read_data()
    datetimeNow=datetime.datetime.now()
    price=data[int(sn)][2].replace("$","")
    total_amount=float(price) * int(num)
    vat='13 %'
    total_afterVAT=total_amount+(0.13*total_amount)
    global GrandTotal
    GrandTotal+=total_afterVAT
    if(os.path.exists(inputed_Name + billNo + '_Bill.txt')):
        with open(inputed_Name  +billNo + '_Bill.txt',"a") as file:
            file.write(f"""
+---------------------------------------------------------+
       Laptop Name : {data[int(sn)][0]}            
       Laptop Brand : {data[int(sn)][1]}           
       Laptop Price: {data[int(sn)][2]}            
       Quantity: {num}                                 
|---------------------------------------------------------|    
        VAT:{vat}                                         
        Total Amount (without VAT):${total_amount}        
|---------------------------------------------------------|
        Total Amount: ${total_afterVAT}                   
                                                          
+---------------------------------------------------------+
           """)
    else:
        with open(inputed_Name+billNo+"_Bill.txt","w") as file:
            file.write(f"""
Company Name: {inputed_Name}
Company Address: {inputed_Address}
Company Contact: {inputed_Contact}    
Sold on :{datetimeNow.strftime("%Y-%m-%d")}  {datetimeNow.strftime("%I")}:{datetimeNow.strftime("%M")}
+---------------------------------------------------------+
         Laptop Name : {data[int(sn)][0]}          
         Laptop Brand : {data[int(sn)][1]}         
         Laptop Price: {data[int(sn)][2]}         
         Quantity: {num}                               
|---------------------------------------------------------|
         VAT:{vat}                                        
         Total Amount (without VAT):${total_amount}       
|---------------------------------------------------------|
         Total Amount: ${total_afterVAT}                  
+---------------------------------------------------------+    
            """)

def grandTotal(company_Name, billNo):
    global GrandTotal
    with open(company_Name +billNo+"_Bill.txt","a")as file:
        file.write(f"""
+---------------------------------------------------------+       
    Grand Total:{GrandTotal}                      
+---------------------------------------------------------+
       """)
GrandTotal=0
    
