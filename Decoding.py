# 🧩 Challenge

# The final hidden message is a plain English phrase encoded in 3 layers:

# Plaintext → ROT13, ROT13 → Base64, Base64 → Hex

# Here’s your encoded string (the only thing you get):

# String in Question 343638363335366336313662363336633633366532303661363936643635366532303633363936373631366532303635366536313631366336313230363136313638363536313663

# 🔎 Your Task 

# First, recognize that this looks like hex (only 0–9 and a–f).

#       Decode from hex to get a Base64 string.

# Second, decode the Base64 string.

#       That will give you something that looks like gibberish.

# Third, apply ROT13 to that gibberish.

#       You should reveal the final English phrase 🎉
#             My attempt below

# import base64, codecs

# msg = "343638363335366336313662363336633633366532303661363936643635366532303633363936373631366532303635366536313631366336313230363136313638363536313663"

# step1 = b64_msg = bytes.fromhex("343638363335366336313662363336633633366532303661363936643635366532303633363936373631366532303635366536313631366336313230363136313638363536313663").decode()
# print("Base64 decoded:", b64_msg)

# step2 = rot_msg = codecs.decode(b64_msg, "rot_13")
# print("ROT13 decoded:", rot_msg)

# step3 = final_msg = base64.b64decode(b64_msg).decode()
# print("Final message:", final_msg)
#           Chat Correction

import base64, codecs

# Hex-encoded string (given)
msg = "343638363335366336313662363336633633366532303661363936643635366532303633363936373631366532303635366536313631366336313230363136313638363536313663"

# Step 1: Hex → Base64
b64_msg = bytes.fromhex(msg).decode()
print("Step 1 (hex → Base64):", b64_msg)

# Step 2: Base64 → ROT13 (still encoded in ROT13)
rot_msg = base64.b64decode(b64_msg).decode()
print("Step 2 (Base64 → ROT13):", rot_msg)

# Step 3: ROT13 → Plaintext
final_msg = codecs.decode(rot_msg, "rot_13")
print("Step 3 (ROT13 → Plaintext):", final_msg)
