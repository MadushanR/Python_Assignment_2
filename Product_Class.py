class Product:

    def __init__(self,product_code,product_name,sale_price,manufacture_cost,stock_level,units_produced,units_sold):
        self.product_code = product_code
        self.product_name = product_name
        self.sale_price = sale_price
        self.manufacture_cost = manufacture_cost
        self.stock_level = stock_level
        self.units_produced = units_produced
        self.units_sold = units_sold

    def display(self):
        print(self.product_code,self.product_name,self.sale_price,self.manufacture_cost,self.stock_level,self.units_sold)


    def setProduct_code(self,product_code):
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

    def getProduct_Code(self):
        print(self.product_code)

    def getProduct_Name(self):
        print(self.product_name)

    def getSale_price(self):
        print(self.sale_price)

    def getManufacture_cost(self):
        print(self.manufacture_cost)

    def getStock_level(self):
        print(self.stock_level)

    def getUnits_produced(self):
        print(self.units_produced)

    def getUnits_Sold(self):
        print(self.units_sold)
    
    

    