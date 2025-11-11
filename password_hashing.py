# Saturday Aug 23, 2025

# Daily Note: Implemented password hashing using Argon2 and Bcrypt. I have started a week earlier than planned. This was supposed to be week 2 day 08/25 but F it we ball. I completed the projects separately.

# I was introduced to the concepts of password hashing and the importance of using strong, adaptive hashing algorithms to protect user credentials. Here's both in one doc

####### INTRODUCING PIP LIST##########
# pip install bcrypt
# pip install argon2-cffi

# password_hashing.py
import bcrypt
from argon2 import PasswordHasher
import time

# --- bcrypt demo ---
password = b"my_secret_password"
salt = bcrypt.gensalt()
hashed = bcrypt.hashpw(password, salt)

print("bcrypt hash:", hashed)

entered_password = b"my_secret_password"
if bcrypt.checkpw(entered_password, hashed):
    print("✅ bcrypt password matches")
else:
    print("❌ bcrypt invalid password")

# --- argon2 demo ---
ph = PasswordHasher()

start = time.time()
argon2_hash = ph.hash("my_secret_password")
print("argon2 hash:", argon2_hash)
print("argon2 time:", time.time() - start)
