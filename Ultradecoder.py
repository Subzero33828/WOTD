# sample encoded message (hex)
msg = "343638363335366336313662363336633633366532303661363936643635366532303633363936373631366532303635366536313631366336313230363136313638363536313663"

import hashlib

def hash_hex_string(hex_string):
    try:
        # Validate input length (must be even number of hex digits)
        if len(hex_string) % 2 != 0:
            return "Error: hex string length must be even."

        # Decode hex string safely
        data = bytes.fromhex(hex_string)

        # Return SHA-256 hash
        return hashlib.sha256(data).hexdigest()

    except ValueError as e:
        return f"Error: invalid hex string. Details: {e}"

# Example usage
print(hash_hex_string("4a6f686e"))  # "John"
print(hash_hex_string("4g"))        # invalid (will trigger error handling)
