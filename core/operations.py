from store.inventory import products_db, product_props_lst, Product
import uuid

operations = {
  1: 'Create: Add new products with details',
  2: 'View all products',
  3: 'Search by ID, name, category',
  4: 'Filter products',
  5: 'Modify product details, update stock quantity',
  6: 'Remove products'
  }

class InvalidRole(Exception):
  pass

def show_menu_by_role(role: str):
  filtered_operations = get_operations_by_role(role)
  print(f'<<< Select an operation to perform by Role[{role}]>>>')
  for key, value in filtered_operations.items():
    print(f'{key} - {value}')
  user_input = int(input('Enter an option: '))
  if user_input not in filtered_operations:
    raise ValueError(f'---------Invalid Operation for role [{role}]----------: {user_input}')
  print(f'Selected: {user_input} -> {filtered_operations[user_input]}')
  if perform_operation(user_input):
    show_menu_by_role(role)

def get_operations_by_role(role: str) -> dict:
    all_operations_by_role = {'user': [2, 3, 4], 'admin': [1, 2, 3, 4, 5, 6]}
    if all_operations_by_role.get(role, None) == None:
      raise InvalidRole
    operation_list_by_role = all_operations_by_role[role]
    filtered_operations = {}
    for operation_idx in operation_list_by_role:
      filtered_operations[operation_idx] = operations[operation_idx]
    return filtered_operations

def perform_operation(user_input: int) -> bool:
  match user_input:
    case 1:
      create_product()
    case 2:
      view_all_products()
    case 3:
      search_by()
    case 4:
      filter_products()
    case 5:
      update_products()
    case 6:
      remove_product()
    case _:
      print('Invalid User Input')

  return True if input('Do You want to repeat again? (Y/N):').lower() == 'y'  else False
 

def create_product():
  product_data = eval(input("Enter Product Details in the format {'name' : 'Product Name', 'category' : 'Stationary'}: "))
  product_data['id'] = uuid.uuid4() # Create Random Product Id
  product = Product(product_data) # Create Product by dictionary constructor
  products_db.append(product)
  print('>>>>>>>>>>>  Product Added to DB  <<<<<<<<<<<<<<')

def view_all_products():
  if len(products_db) == 0:
    print('No Products available to view')
    return
  print('Viewing All Products')
  display_products(products_db)
    
def search_by():
  '''
  Accepts Keyword to search from keyboard and 
  find matching products based on name and category
  '''
  if len(products_db) == 0:
    print('No Products available to search')
    return
  keyword = input('Enter a keyword to search: ').lower()
  matched_products = [ product for product in products_db if any(keyword in str.lower() for str in [str(product.id), product.name, product.category])]
  # matched_products = [ product for product in products_db if keyword in product.name.lower() or keyword in product.category.lower()]
  if matched_products:
    display_products(matched_products)
  else:
    print(f':-( No Product Found for input string[{keyword}]')

def display_products(products):
    for product in products:
      print(f'{product.id} | {product.name:20} | {product.category:40} | {product.price:5.2f} | {product.quantity:4d}')

def filter_products():
  '''
  Filter products by price range
  '''
  if len(products_db) == 0:
    print('No Products available to Filter')
    return
  min = eval(input('Enter Minimum price :'))
  max = eval(input('Enter Maximum price :'))
  print(f'Min[{min}], Max[{max}]')
  filtered_products = [ product for product in products_db if min <= product.price <= max]
  if filtered_products:
    display_products(filtered_products)
  else:
    print(f':-( No Products Found in the price range[{min}:{max}]')

def update_products():
  if len(products_db) == 0:
    print('No Products available to update')
    return
  product_data = eval(input("Enter Product detail with mandatory Id and fields to update {'id' : '4f844eaa', 'category' : 'Stationary'}: "))
  product_to_update = None
  if product_data.get('id') is None:
    raise AttributeError('Missing Mandatory Attribute[id]')
  for product in products_db:
    if str(product.id) == product_data.get('id'):
      product_to_update = product
      break
  if product_to_update:
    for attribute in product_props_lst:
      if product_data.get(attribute) is not None:
        setattr(product_to_update, attribute, product_data.get(attribute))
    print('>>>>>>>>>>>  Product Updated to DB  <<<<<<<<<<<<<<')
  else:
    print(f'No Product Matching the Given Id[{product_data.get('id')}]')

def remove_product():
  if len(products_db) == 0:
    print('No Products available to delete/remove from DB')
    return
  product_id = input('Enter the Product ID to remove :')
  product_to_remove = None
  for product in products_db:
    if str(product.id) == product_id:
      product_to_remove = product
      break
  if product_to_remove:
      products_db.remove(product_to_remove)
      print(f'Removed Product {product_to_remove}')