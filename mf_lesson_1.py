# Features
# 1. Register - DONE
# 2. Login - DONE
# 3. List products - DONE
# 4. Add to cart - TODO
# 5. Checkout - TODO

user_db = []
item_db = [
    {"name":"iPhone", "price":23},
    {"name":"Samsung", "price":23},
    {"name":"iPhone", "price":23},
    {"name":"iPhone", "price":23},
    {"name":"iPhone", "price":23},
    {"name":"iPhone", "price":23},
]

# Query functions
def create_user(fullname, username, password):
    for user in user_db:
        if username == user["username"]:
            return False
    
    # Create the new user
    new_user = {"fullname":fullname, "username": username, "password":password}
    # Add the new user to the db
    user_db.append(new_user)
    return new_user

def get_user(username):
    for user in user_db:
        if user["username"] == username:
            return user 
    return False

def login_user(username, password):
    for user in user_db:
        if user["username"] == username and user["password"] == password:
            return user 
    return False

# Auth functions
def register():
    print("=====================================")
    print("Registration Page")
    print("=====================================")
    fullname = input("Fullname : ")
    username = input("Username : ")
    password = input("Password : ")
    # Create the user
    user = create_user(fullname, username, password)
    if user:
        login()
    else:
        print("Username not available")
        print("Try Again")
        register()


def login():
    print("=====================================")
    print("Login Page")
    print("=====================================")
    username = input("Username : ")
    password = input("Password : ")
    user = login_user(username, password)
    if user:
        main_page()
    else:
        print("Invalid username and password provided. Please try again")
        login()

def auth():

    print("""
    1. Register 2. Login
    """)
    user_input = input("Response: ")
    if user_input == "1":
        register()
    elif user_input =="2":
        login()
    else:
        print("Wrong input")

# Main page
def main_page():
    count = 1
    for item in item_db:
        print(count, item['name'])
        count = count +1
    


def app():
    auth()




# Running app
app()