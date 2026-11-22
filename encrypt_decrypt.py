#!/usr/bin/env python3
"""
Encrypt/Decrypt tasks.csv using Fernet (symmetric encryption)
Secure, simple, and cloud-friendly
"""

import os
import sys
from cryptography.fernet import Fernet

def generate_key():
    """Generate a new encryption key"""
    key = Fernet.generate_key()
    return key.decode()

def encrypt_file(input_file, output_file, key):
    """Encrypt a file"""
    cipher = Fernet(key.encode())
    with open(input_file, 'rb') as f:
        data = f.read()
    encrypted = cipher.encrypt(data)
    with open(output_file, 'wb') as f:
        f.write(encrypted)
    print(f"✓ Encrypted: {input_file} → {output_file}")

def decrypt_file(input_file, output_file, key):
    """Decrypt a file"""
    cipher = Fernet(key.encode())
    with open(input_file, 'rb') as f:
        encrypted = f.read()
    try:
        decrypted = cipher.decrypt(encrypted)
        with open(output_file, 'wb') as f:
            f.write(decrypted)
        print(f"✓ Decrypted: {input_file} → {output_file}")
        return True
    except Exception as e:
        print(f"✗ Decryption failed: {e}")
        return False

def get_encryption_key_from_env():
    """Get encryption key from environment variable"""
    key = os.environ.get('ENCRYPTION_KEY')
    if not key:
        print("ERROR: ENCRYPTION_KEY environment variable not set")
        return None
    return key

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python encrypt_decrypt.py generate         # Generate new key")
        print("  python encrypt_decrypt.py encrypt          # Encrypt tasks.csv")
        print("  python encrypt_decrypt.py decrypt          # Decrypt tasks.csv.enc")
        sys.exit(1)

    action = sys.argv[1]

    if action == "generate":
        key = generate_key()
        print("\n🔑 NEW ENCRYPTION KEY (SAVE THIS SECURELY):")
        print("=" * 60)
        print(key)
        print("=" * 60)
        print("\nStore this key as ENCRYPTION_KEY in GitHub Secrets")

    elif action == "encrypt":
        key = os.environ.get('ENCRYPTION_KEY') or generate_key()
        if not os.path.exists('Input/tasks.csv'):
            print("ERROR: Input/tasks.csv not found")
            sys.exit(1)
        encrypt_file('Input/tasks.csv', 'Input/tasks.csv.enc', key)

    elif action == "decrypt":
        key = get_encryption_key_from_env()
        if not key:
            sys.exit(1)
        if not os.path.exists('Input/tasks.csv.enc'):
            print("ERROR: Input/tasks.csv.enc not found")
            sys.exit(1)
        decrypt_file('Input/tasks.csv.enc', 'tasks_decrypted.csv', key)
