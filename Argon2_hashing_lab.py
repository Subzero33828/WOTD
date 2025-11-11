from argon2 import PasswordHasher
import time

# Step 3: Compare bcrypt and Argon2 hashing times
ph = PasswordHasher()

# bcrypt
start = time.time()
bcrypt.hashpw(password, bcrypt.gensalt())
print("⏳ bcrypt time:", time.time() - start)

# argon2
start = time.time()
argon2_hash = ph.hash("my_secret_password")
print("argon2 hash:", argon2_hash)
print("⏳ argon2 time:", time.time() - start)

#✅ Checkpoint: You should see two timings.#Argon2 may take slightly longer, but it’s designed to be memory-hard (slows down GPU brute force).

    # Step 4 — Play Around

    # Change password to something else.

    # Re-run and see how the hashes change (even for the same password, the hash will differ because of salting).

    # Try increasing bcrypt’s rounds:

    # bcrypt.gensalt(rounds=14)


    # (Slower, but more secure.)

#     ⚡ By the end of this lab, you should be able to:

# Hash passwords with bcrypt.

# Verify user login attempts.

# Compare bcrypt vs Argon2.

# Explain why salting + slow hashing = better security.