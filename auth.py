import hashlib

users = {}

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register(username, password):
    if not username or not password:
        print("Username and password cannot be empty.")
        return False
    if username in users:
        print("Username already exists.")
        return False
    users[username] = hash_password(password)
    print("User registered successfully.")
    return True

def login(username, password):
    if not username or not password:
        print("Username and password cannot be empty.")
        return False
    if username not in users:
        print("Username not found.")
        return False
    if users[username] != hash_password(password):
        print("Incorrect password.")
        return False
    print("Login successful.")
    return True
