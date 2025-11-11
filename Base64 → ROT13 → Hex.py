Got it ✅ — I’ll hold the **bcrypt/argon2 mini-labs** for later, and we can circle back to refine them into one polished lab.

For **today’s project (Tue 8/26 CTF)** here’s a solid breakdown and combined notes to guide you:

---

## 🔑 Core Concepts

 **Encoding vs. Encryption**

   * **Encoding** = making data fit a format (Base64, Hex, ROT13). Not secret, just transformation.

   * **Encryption** = making data secret (AES, RSA). Needs a key to reverse.

   * **Hashing** = one-way transformation (bcrypt, Argon2). Can’t be unhashed or reversed.

1. **Base64**

   * Represents binary data in text (A–Z, a–z, 0–9, +, /).

   * Common in emails, JSON web tokens, and CTFs.

   * Easy to decode in Python:

  ``python
     import base64
     base64.b64decode("SGVsbG8gV29ybGQh").decode()
     # 'Hello World!'
     ```

2. **ROT13**

   * Caesar cipher shift of 13 characters.

   * Easy to reverse (apply ROT13 twice = original message).

   * Python 3:

     ```python
     import codecs
     codecs.decode("Uryyb Jbeyq!", "rot_13")
     # 'Hello World!'
     ```

3. **Chaining Encodings**

   * CTF challenges often **nest** encodings: Example: Base64 → ROT13 → Hex.

   * Strategy: decode step-by-step, check if output “looks like” another encoding (printable ASCII, lots of A–F digits, `=` padding, etc.).

---

## 🛠️ Mini Lab Plan

### Step 1: Decode Base64
```python
import base64

msg = "U29tZSBzZWNyZXQgbWVzc2FnZQ=="  # "Some secret message"
decoded = base64.b64decode(msg).decode()
print("Base64 decoded:", decoded)
```

### Step 2: Decode ROT13
```python
import codecs

rot_msg = "Uryyb Jbeyq!"  # ROT13 of "Hello World!"
decoded = codecs.decode(rot_msg, "rot_13")
print("ROT13 decoded:", decoded)
```

### Step 3: Chain Them Together
```python
import base64, codecs

msg = "Vnlyb2ggUGJjcSE="  # this is ROT13 after base64
step1 = base64.b64decode(msg).decode()
print("Step1 (base64):", step1)

step2 = codecs.decode(step1, "rot_13")
print("Step2 (rot13):", step2)
```

---

## ⚡ Stretch Ideas
* Add **hex decoding**:

  ```python
  bytes.fromhex("48656c6c6f").decode()
  # 'Hello'
  ```
* Add **URL decoding**:

  ```python
  from urllib.parse import unquote
  unquote("Hello%20World%21")
  # 'Hello World!'
  ```
* Write a **decoder chain function** that tries multiple encodings in sequence until it finds a readable message.

---

✅ By the end, you should:

* Be able to explain difference between encoding/encryption/hashing.
* Decode Base64 and ROT13 manually in Python.
* Solve “chained” encodings step-by-step like in real CTFs.

---

Do you want me to **set up a challenge string for you to decode** (like a mini-CTF puzzle you can run through Base64 → ROT13 → Hex), or would you rather just start with the step-by-step code skeleton and build your own challenges?
