class User:
  def __init__(self, username, role):
    self._username = username
    self._role = role

  @property
  def username(self):
    return self._username
  
  @username.setter
  def username(self, username):
    self._username = username

  @property
  def role(self):
    return self._role
  
  @role.setter
  def role(self, role):
    self._role = role
    
USERS = {
  User('sathish', 'admin'),
  User('rajesh', 'user'),
  User('bijesh', 'super_user') # InvalidRoleError
}