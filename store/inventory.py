from store.product import Product

class Inventory:
   
   def __init__(self, initial_products=None):
        self._products = initial_products if initial_products is not None else []

   @property
   def products(self):
      return self._products
   
   @products.setter
   def products(self, products):
      if not isinstance(products, list):
         return
      if any(not isinstance(item, Product) for item in products):
         return
      self._products = products

   def add_product(self, product: Product):
      self._products.append(product)
   
   def update_product(self, product_data:dict) -> bool:
      product_to_update = None
      for product in self._products:
         if str(product.id) == product_data.get('id'):
            product_to_update = product
            break
      if product_to_update:
         for attribute in Product.PRODUCT_PROPERTYS:
            if product_data.get(attribute) is not None:
               setattr(product_to_update, attribute, product_data.get(attribute))
         return True
      else:
         return False
   
   def remove_product(self, product_id: str) -> bool:
      product_to_remove = None
      for product in self._products:
         if str(product.id) == product_id:
            product_to_remove = product
            break
      if product_to_remove:
         self._products.remove(product_to_remove)
         return True
      else:
         return False