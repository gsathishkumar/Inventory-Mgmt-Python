from store.product import Product
from store.inventory import Inventory
from store.user import User, USERS
from store.exceptions import UserNotFoundError, InvalidRoleError
import uuid

operations = {
  1: 'Create: Add new products with details',
  2: 'View all products',
  3: 'Search by ID, name, category',
  4: 'Filter products',
  5: 'Modify product details, update stock quantity',
  6: 'Remove products'
  }
all_operations_by_role = {'admin': [1, 2, 3, 4, 5, 6], 'user': [2, 3, 4]}

def select_user():
  user_input = input('Enter Username: ')
  for user in USERS:
    if user_input.lower() == user.username.lower():
      return user
  else:
    raise UserNotFoundError(f'---------Invalid User----------: {user_input}')
  
def show_menu(user: User):
  filtered_operations = get_operations_by_role(user.role)
  print(f'<<< Select an operation to perform by Role[{user.role}]>>>')
  for key, value in filtered_operations.items():
    print(f'{key} - {value}')
  user_input = int(input('Enter an option: '))
  if user_input not in filtered_operations:
    raise ValueError(f'---------Invalid Operation for role [{user.role}]----------: {user_input}')
  print(f'Selected: {user_input} -> {filtered_operations[user_input]}')
  if perform_operation(user_input):
    show_menu(user)

def get_operations_by_role(role: str) -> dict:
    if all_operations_by_role.get(role, None) == None:
      raise InvalidRoleError(f'---------Invalid User Role [{role}]----------')
    operation_list_by_role = all_operations_by_role[role]
    filtered_operations = {}
    for operation_idx in operation_list_by_role:
      filtered_operations[operation_idx] = operations[operation_idx]
    return filtered_operations

def perform_operation(user_input: int) -> bool:
  match user_input:
    case 1:
      show_create_product()
    case 2:
      view_all_products()
    case 3:
      show_search_by()
    case 4:
      show_filter_products()
    case 5:
      show_update_product()
    case 6:
      show_remove_product()
    case _:
      print('Invalid User Input')

  return True if input('Do You want to repeat again? (Y/N):').lower() == 'y'  else False
 

def show_create_product():
  product_data = eval(input("Enter Product Details in the format {'name' : 'Product Name', 'category' : 'Stationary'}: "))
  product_data['id'] = uuid.uuid4() # Create Random Product Id
  product = Product(product_data) # Create Product by dictionary constructor
  inventory.add_product(product)
  print('>>>>>>>>>>>  Product Added to Store  <<<<<<<<<<<<<<')

def view_all_products():
  if len(inventory.products) == 0:
    print('No Products available to view')
    return
  print('Viewing All Products')
  display_products(inventory.products)
    
def show_search_by():
  if len(inventory.products) == 0:
    print('No Products available to search')
    return
  keyword = input('Enter a keyword to search: ').lower()
  matched_products = [ product for product in inventory.products if any(keyword in str.lower() for str in [str(product.id), product.name, product.category])]
  if matched_products:
    display_products(matched_products)
  else:
    print(f':-( No Product Found for input string[{keyword}]')

def display_products(products):
    for product in products:
      print(f'{product.id} | {product.name:20} | {product.category:40} | {product.price:5.2f} | {product.quantity:4d}')

def show_filter_products():
  if len(inventory.products) == 0:
    print('No Products available to Filter')
    return
  min = eval(input('Enter Minimum price :'))
  max = eval(input('Enter Maximum price :'))
  print(f'Min[{min}], Max[{max}]')
  filtered_products = [ product for product in inventory.products if min <= product.price <= max]
  if filtered_products:
    display_products(filtered_products)
  else:
    print(f':-( No Products Found in the price range[{min}:{max}]')

def show_update_product():
  if len(inventory.products) == 0:
    print('No Products available to update')
    return
  product_dict = eval(input("Enter Product detail with mandatory Id and fields to update {'id' : '4f844eaa', 'category' : 'Stationary'}: "))
  if product_dict.get('id') is None:
    raise AttributeError('Missing Mandatory Attribute[id]')
  if inventory.update_product(product_dict):
    print('>>>>>>>>>>>  Product Updated to Store  <<<<<<<<<<<<<<')
  else:
    print(f'No Product Matching the Given Id[{product_dict.get('id')}]')

def show_remove_product():
  if len(inventory.products) == 0:
    print('No Products available to delete/remove from DB')
    return
  product_id = input('Enter the Product ID to remove :')
  if inventory.remove_product(product_id):
    print('>>>>>>>>>>> Product Removed from Store  <<<<<<<<<<<<<<')
  else:
    print(f'No Product Matching the Given Id[{product_id}]')

def load_inventory(load_sample: bool )-> Inventory:
  global inventory
  sample_products = [
    {'id':'b28bfe29-cc21-494e-a945-14c18a96abc6','name' : 'Eraser', 'category' : 'stationary', 'price': 2 , 'quantity': 20},
    {'id':'b29bfe30-cc22-495e-a946-14c18a97abc7','name' : 'Pencil', 'category' : 'stationary', 'price': 5 , 'quantity': 100},
    {'id':'b30bfe31-cc23-496e-a947-14c18a98abc8','name' : 'Lipstick', 'category' : 'beauty', 'price': 10 , 'quantity': 10},
    {'id':'b31bfe32-cc24-497e-a948-14c18a99abc9','name' : 'Brown eggs', 'category' : 'dairy', 'price': 20.5 , 'quantity': 5},
    {'id':'b32bfe33-cc25-498e-a949-14c18a94abc0','name' : 'Strawberry', 'category' : 'fruit', 'price': 50 , 'quantity': 10},
    {'id':'b33bfe34-cc26-499e-a950-14c18a95abc5','name' : 'apple', 'category' : 'fruit', 'price': 99.58 , 'quantity': 30}
  ]
  if load_sample:
    products = [Product(product_dict) for product_dict in sample_products]
    inventory = Inventory(products)
  else: 
    inventory = Inventory()