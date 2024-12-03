import random
import string

def generate_password(lenth: int = 16):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(alphabet) for i in range(lenth))
    return password 
password = generate_password()
print(f"Generated Password: {password}")