import hashlib

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def login(email: str, password_to_check: str, stored_logins: dict) -> bool:
    """
    Checks if the provided password matches the stored hash for the given email.
    
    :param email: The email of the user trying to log in.
    :param password_to_check: The password input by the user.
    :param stored_logins: A dictionary containing email-password hash pairs.
    :return: True if the password matches, False otherwise.
    """
    if email not in stored_logins:
        return False  # Email not found in stored logins
    
    hashed_input_password = hash_password(password_to_check)
    return stored_logins[email] == hashed_input_password  # Check if hashes match

# Example Usage
stored_logins = {
    "user@example.com": hash_password("securepassword123"),
    "admin@example.com": hash_password("adminsecurepass")
}

print(login("user@example.com", "securepassword123", stored_logins))  # True
print(login("user@example.com", "wrongpassword", stored_logins))  # False
