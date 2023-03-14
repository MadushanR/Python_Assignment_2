import Product_Class

product_code = int(input("Enter product code "))
while product_code<100 or product_code>1000:
    product_code = int(input("Enter a product code between 100 and 1000 "))

product_name = input("Enter product name ")

stock_level = int(input("Enter stock level "))
while stock_level < 0 :
    stock_level = int(input("Enter stock level greater than 0 "))

sale_price = float(input("Enter sale price "))
while sale_price<0:
    sale_price = float(input("Enter a sale price greater than 0 "))

manufacture_cost = float(input("Enter manufacture cost "))
while manufacture_cost<0:
    manufacture_cost = float(input("Enter manufacture cost greater than 0 "))

units_produced = int(input("Enter estimated montly production "))
while units_produced < 0:
    units_produced = int(input("Enter estimated montly production greater than 0 "))


P1 = Product_Class.Product(product_code,product_name,sale_price,manufacture_cost,stock_level,units_produced,0)


P1.display()


