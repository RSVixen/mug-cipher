from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64

# Key size for AES (e.g., 256-bit key)
KEY_SIZE = 32  # 256 bits
BLOCK_SIZE = AES.block_size

def generate_key():
    """Generate a random 256-bit key"""
    return get_random_bytes(KEY_SIZE)

def encrypt(data, key):
    """Encrypt data with AES using CBC mode"""
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(data.encode(), BLOCK_SIZE))
    iv = base64.b64encode(cipher.iv).decode('utf-8')
    ct = base64.b64encode(ct_bytes).decode('utf-8')
    return iv, ct

def decrypt(iv, ct, key):
    """Decrypt AES encrypted data"""
    iv = base64.b64decode(iv)
    ct = base64.b64decode(ct)
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    decrypted_data = unpad(cipher.decrypt(ct), BLOCK_SIZE).decode()
    return decrypted_data

if __name__ == "__main__":
    # Example usage
    key = generate_key()  # Generate a random key

    data = "This is a secret message"
    iv, encrypted_data = encrypt(data, key)
    print(f"Encrypted: {encrypted_data}")

    decrypted_data = decrypt(iv, encrypted_data, key)
    print(f"Decrypted: {decrypted_data}")
