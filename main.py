
from dotenv import load_dotenv
from operations import select_user, show_menu, load_inventory
from utils import get_bool_env

inventory = None;

# Load variables from the .env file
load_dotenv()

if __name__ == '__main__':
  print('Welcome to Inventory Management System')
  load_inventory(get_bool_env("init_products"))
  try:
    user = select_user()
    show_menu(user)
  except Exception as e:
    print(e)