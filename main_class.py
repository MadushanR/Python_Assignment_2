import Product_Class
import random

print("Welcome to Programming Principles Sample Product Inventory")
product_code = int(input("Please enter the Product Code : "))
while product_code<100 or product_code>1000 :
    product_code = int(input("Enter a product code between 100 and 1000 : "))

product_name = input("Please enter the Product Name : ")

stock_level = int(input("Please enter the Current Stock Level : "))
while stock_level < 0 :
    stock_level = int(input("Enter stock level greater than 0 : "))

sale_price = float(input("Please enter the Product Sale Price : "))
while sale_price<0:
    sale_price = float(input("Enter a sale price greater than 0 : "))

manufacture_cost = float(input("Please enter the Manufacture Cost : "))
while manufacture_cost<0:
    manufacture_cost = float(input("Enter manufacture cost greater than 0 : "))

units_produced = int(input("Please enter estimated montly production : "))
while units_produced < 0:
    units_produced = int(input("Enter estimated montly production greater than 0 : "))


P1 = Product_Class.Product(product_code,product_name,sale_price,manufacture_cost,stock_level,units_produced,0)

print("\n********Programming Principles Sample Stock Statement*******")

print("\nProduct Code : " , P1.getProduct_Code())
print("Product Name : " , P1.getProduct_Name())
print("\nSale Price : " , P1.getSale_price() , " CAD ")
print("Manufacture Cost: " , P1.getManufacture_cost() , " CAD")
print("Monthly Production: " , P1.getUnits_produced() , " units (Approx.) \n")

month = 1
total_sold = 0
while month <13:
    print("Month ", month , " :")
    print("   Manufactured : ", P1.getUnits_produced() , " units")
    sold = random.randint(int(P1.getUnits_produced())-10,int(P1.getUnits_produced())+10)
    total_sold = total_sold + sold
    print("   Sold : ", sold , " units")
    stock = int(P1.getStock_level()) + int(P1.getUnits_produced()) - sold
    P1.setStock_Level(stock)
    print( "   Stock : ", stock , " units")
    month = month + 1

net_profit = (total_sold * int(P1.getSale_price())) - (12 * int(P1.getUnits_produced())* int(P1.getManufacture_cost()))
print("\n Net Profit : " , net_profit , " CAD")
