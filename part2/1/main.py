username = input("Enter your username: ")
password = input("Enter your password: ")

if username != "admin":
  print("user not found")
elif password != "admin":
  print("incorrect password")
else:
  print("successful login")