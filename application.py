import Product_Class #imports Class Product
import random #imports random library

print("Welcome to Programming Principles Sample Product Inventory")
product_code = int(input("Please enter the Product Code : ")) #gets product code input
while product_code<100 or product_code>1000 : #validates input
    product_code = int(input("Enter a product code between 100 and 1000 : "))

product_name = input("Please enter the Product Name : ") #gets product name input

stock_level = int(input("Please enter the Current Stock Level : ")) #gets stock level input
while stock_level < 0 : #validates input
    stock_level = int(input("Enter stock level greater than 0 : "))

sale_price = float(input("Please enter the Product Sale Price : ")) #gets sale price input
while sale_price<0: #validates input
    sale_price = float(input("Enter a sale price greater than 0 : "))

manufacture_cost = float(input("Please enter the Manufacture Cost : ")) #gets manufacture cost input
while manufacture_cost<0: #validates input
    manufacture_cost = float(input("Enter manufacture cost greater than 0 : "))

units_produced = int(input("Please enter estimated montly production : ")) #gets montly production input
while units_produced < 0: #validates input
    units_produced = int(input("Enter estimated montly production greater than 0 : "))


P1 = Product_Class.Product(product_code,product_name,sale_price,manufacture_cost,stock_level,units_produced,0) #calls construct method with given arguments in product class

print("\n********Programming Principles Sample Stock Statement*******")

print("\nProduct Code : " , P1.getProduct_Code()) #prints product code using get method in product class
print("Product Name : " , P1.getProduct_Name()) #prints product name using get method in product class 
print("\nSale Price : " , P1.getSale_price() , " CAD ") #prints sale price using get method in product class
print("Manufacture Cost: " , P1.getManufacture_cost() , " CAD") #prints manufacture cost using get method in product class
print("Monthly Production: " , P1.getUnits_produced() , " units (Approx.) \n") #prints units produced using get method in product class

month = 1 #intializes month to 1
total_sold = 0 #initializes total sold products to 0
not_sold = [] #initializes a list to store failed sales month due to less stock
while month <13: #checks if month is less than 13

    print("Month ", month , " :")
    print("|   Manufactured : ", P1.getUnits_produced() , " units") #prints units produced using get method in product class
    sold = random.randint(int(P1.getUnits_produced())-10,int(P1.getUnits_produced())+10) #generates a random number between +/- 10 of units produced as sales
    if (int(P1.getStock_level())+int(P1.getUnits_produced())) >= sold : #check if there is enough stock for sale
        total_sold = total_sold + sold #adds total sold with sold
        print("|   Sold : ", sold , " units") 
        stock = int(P1.getStock_level()) + int(P1.getUnits_produced()) - sold #calculates current stock after sales
        P1.setStock_Level(stock) #stores the currect stock to product object
        print( "|   Stock : ", stock , " units")
    else :
        stock = int(P1.getStock_level()) + int(P1.getUnits_produced()) #calculates current stock
        P1.setStock_Level(stock) #stores the currect stock to product object
        print("|   Product required is ", sold , " but stock available is only", stock)
        not_sold.append(month) #appends the failed sales month list
    month = month + 1 #increments month

net_profit = (total_sold * int(P1.getSale_price())) - (12 * int(P1.getUnits_produced())* int(P1.getManufacture_cost())) #calculates net profit by total sales and total productions
if net_profit > 0 : #checks if it is profit or loss to display relevant message
    print("\n Net Profit : " , net_profit , " CAD")
else :
    print("\n Net Loss : " , net_profit , " CAD")

if len(not_sold) < 1 : #displays the failed sales month list
    print("\n No failed sales")
else :
    print("\n Products were not sold in below months due to no stock :")
    for i in not_sold:
        print(" ",i)
