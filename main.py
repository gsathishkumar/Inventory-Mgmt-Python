from login.options import select_role
from core.operations import show_menu_by_role

if __name__ == '__main__':
  print('Welcome to Inventory Management System')
  try:
    show_menu_by_role(select_role())
  except ValueError as e:
    print(e)
