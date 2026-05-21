username = input("enter username: ")
password = input("enter password: ")

correct_username = "admin"
correct_password = "1234"

if(username == correct_username and password == correct_password):
    print("login successfully")

else:
    print("invalid username or password")