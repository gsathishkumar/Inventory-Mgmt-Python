class Product:
   PRODUCT_PROPERTYS = ['id', 'name', 'category', 'price', 'quantity']
   def __init__(self, data):
      for property, value in data.items():
         if property in Product.PRODUCT_PROPERTYS:
            setattr(self,property, value )

   @property
   def price(self):
     return self._price
   
   @price.setter
   def price(self, price):
      if price <= 0:
         raise ValueError('Price cannot be negative')
      self._price = price

   def __str__(self):
      return f'{self.id}|{self.name}|{self.category}|{self.price}|{self.quantity}'