class Product: #creates Product class

    def __init__(self,product_code,product_name,sale_price,manufacture_cost,stock_level,units_produced,units_sold): #constructor
        self.product_code = product_code
        self.product_name = product_name
        self.sale_price = sale_price
        self.manufacture_cost = manufacture_cost
        self.stock_level = stock_level
        self.units_produced = units_produced
        self.units_sold = units_sold

    def display(self): #displays all variables of the Product class
        print(self.product_code,self.product_name,self.sale_price,self.manufacture_cost,self.stock_level,self.units_sold)


    def setProduct_code(self,product_code): #setter
        self.product_code = product_code

    def setProduct_name(self,product_name):
        self.product_name = product_name

    def setSale_Price(self,sale_price):
        self.sale_price = sale_price

    def setManufacture_cost(self,manufacture_cost):
        self.manufacture_cost = manufacture_cost

    def setStock_Level(self,stock_level):
        self.stock_level = stock_level

    def setUnits_Produced(self,units_produced):
        self.units_produced = units_produced

    def setUnits_Sold(self,units_sold):
        self.units_sold = units_sold 

    def getProduct_Code(self): #getter
        return self.product_code

    def getProduct_Name(self):
        return self.product_name

    def getSale_price(self):
        return self.sale_price

    def getManufacture_cost(self):
        return self.manufacture_cost

    def getStock_level(self):
        return self.stock_level

    def getUnits_produced(self):
        return self.units_produced

    def getUnits_Sold(self):
        return self.units_sold
    
    

    