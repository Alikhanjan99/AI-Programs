def test_password(password):
  # Set the minimum length and strength requirements
  min_length = 8
  min_strength = 3

  # Initialize variables to track the password strength
  length = 0
  strength = 0
  
  # Check the length of the password
  if len(password) >= min_length:
    length = 1
  
  # Check the strength of the password
  if any(char.isdigit() for char in password):
    strength += 1
  if any(char.isupper() for char in password):
    strength += 1
  if any(char.islower() for char in password):
    strength += 1
  if any(char in '!@#$%^&*()_-+={}[]|\:;"<>,.?/~`' for char in password):
    strength += 1
  
  # Determine if the password meets the requirements
  if length and strength >= min_strength:
    return True
  else:
    return False

# Test the function
password = input('Enter a password: ')
if test_password(password):
  print('Password is valid.')
else:
  print('Password is not valid. Please try again.')
