# Hash a password using the MD5 algorithm:
import hashlib

secret = "This is the password or the document text"
bsecret = secret.encode()
m = hashlib.md5()
m.update(bsecret)
m.digest()

print(m.digest())

# The `cryptography` library is a popular choice for handling encryption problems in
# Python.
#
# `Symmetric key encryption`(对称密钥加密) is a group of encryption algorithms based on a
# shared key.
# AES, Blowfish, DES, Serpent, Twofish
# A shared key is similar to a password that is used to both encrypt and decrypt text.
#

# Fernet is an implementation of the popular AES algorithm
from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)

message = b"Hello World!!!"

encrypted = f.encrypt(message)
print(encrypted)

decrypted = f.decrypt(encrypted)
print(decrypted)

# `Asymmetric key encryption` uses a pair of keys, one public and one private.
# The public key is designed to be widely shared, while a single user holds the private one.
# The only way you can decrypt messages that have been encryped using your public key is by
# using your private key.
# This style of encryption is widely used to pass information confidentially both on local
# networs and across the internet.
# One very popular asymmetric key algorithm is Rivest-Shamir-Adleman(RSA), which is widely
# used for communication across networks.
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa

private_key = rsa.generate_private_key(public_exponent=65537,
                                       key_size=4096,
                                       backend=default_backend())

print(private_key)
public_key = private_key.public_key()
print(public_key)

message = b"HELLO WORLD!"

from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

encrypted = public_key.encrypt(
    message,
    padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                 algorithm=hashes.SHA256(),
                 label=None))

print(encrypted)
decrypted = private_key.decrypt(
    encrypted,
    padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                 algorithm=hashes.SHA256(),
                 label=None))

print(decrypted)
