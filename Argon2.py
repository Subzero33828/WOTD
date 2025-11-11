from argon2 import PasswordHasher
import time

ph = PasswordHasher()

# Argon2 style
start = time.time()
ph.hash("my_secret_password")
print("Argon2 time:", time.time() - start)

# bycript style
# start = time.time()
# bcrypt.hashpw(password, bcrypt.gensalt())
# print("Bcrypt time:", time.time() - start)