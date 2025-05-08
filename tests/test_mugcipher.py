import os
import unittest

class TestMugCipherSetup(unittest.TestCase):

    def test_project_structure(self):
        # Check if core module folders exist
        self.assertTrue(os.path.isdir("mugcipher"))
        self.assertTrue(os.path.isdir("cli"))
        self.assertTrue(os.path.isdir("tests"))
        self.assertTrue(os.path.isdir("docs"))

    def test_core_modules(self):
        # Check if core modules exist
        self.assertTrue(os.path.isfile("mugcipher/encryption.py"))
        self.assertTrue(os.path.isfile("mugcipher/key_manager.py"))
        self.assertTrue(os.path.isfile("mugcipher/file_handler.py"))
        self.assertTrue(os.path.isfile("mugcipher/utils.py"))

    def test_cli_module(self):
        # Check if CLI module exists
        self.assertTrue(os.path.isfile("cli/mugcipher_cli.py"))

if __name__ == '__main__':
    unittest.main()
