def select_role():
  print('Select an user type to login')
  print('1. Admin')
  print('2. User')
  user_input = int(input('Enter an option: '))

  if user_input == 1:
    return 'admin'
  elif user_input == 2:
    return 'user'
  else:
    raise ValueError(f'---------Invalid Option----------: {user_input}')