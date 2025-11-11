# start: 08/23/2025
# Due: 08/25/2025

import bcrypt

#Step 1 hash pswd
password = b"my_secret_password" # RAW password must be bytes
salt = bcrypt.gensalt()  #generate random salt

# what is "salt"?
# Salt is random data that is used as an additional input to a one-way function that hashes a password or passphrase.
# The purpose of salt is to defend against dictionary attacks and rainbow table attacks.

#define rainbow table attack
# A rainbow table attack is a precomputed table for reversing cryptographic hash functions, primarily for cracking password hashes.

hashed = bcrypt.hashpw(password, salt)

print("🔑 Hashed password:", hashed)

#✅ Checkpoint: You should see a long hash string like b'$2b$12$...'.Notice: It’s different each time you run (because of the random salt).

# Step 2: Verify a password against the stored hash
entered_password = b"my_secret_password"   # try changing this to a wrong password

if bcrypt.checkpw(entered_password, hashed):
    print("✅ Password matches")
else:
    print("❌ Invalid password")
