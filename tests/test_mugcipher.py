import unittest
from mugcipher.encryption import generate_key, encrypt, decrypt

class TestEncryption(unittest.TestCase):

    def test_encryption_decryption(self):
        # Generate a random key
        key = generate_key()

        # Test data
        data = "Hello, Mug Cipher!"

        # Encrypt the data
        iv, encrypted_data = encrypt(data, key)
        self.assertNotEqual(encrypted_data, data)  # Ensure it's encrypted

        # Decrypt the data
        decrypted_data = decrypt(iv, encrypted_data, key)
        self.assertEqual(decrypted_data, data)  # Ensure it matches original data

if __name__ == '__main__':
    unittest.main()
