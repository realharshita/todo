import hashlib

users = {}

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register(username, password):
    if username in users:
        print("Username already exists.")
        return False
    users[username] = hash_password(password)
    print("User registered successfully.")
    return True
