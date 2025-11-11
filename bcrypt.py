import bcrypt

# User registers → hash their password
password = b"my_secret_passowrd"
salt = bcrypt.gensalt()
hashed = bcrypt.hashpw(password, salt)

print("Hashed password", hashed)

#  User logs in → check their password
entered_password = b"my_secret_password"
if bcrypt.checkpw(entered_password, hashed):
    print("✅ Password matches")
else:
    print("❌ Invalid password")