#TUPLE
users = (("rupa","pass12"),)

# Login function
def login(username, password):
    details = (username, password)
    if details in users:
        print("Login successful! Welcome,", username)
    else:
        print("Login failed! Invalid username or password.")

# Try logging in
login("rupa","pass12") # Success

