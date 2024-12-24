from nacl.secret import SecretBox
from nacl.utils import random
import hashlib

def expand_key(user_key):
	return hashlib.sha256(user_key.encode()).digest() # expand key by hashing to 32 bytes

def ft_encrypt(user_key, content):
	key = expand_key(user_key)
	box = SecretBox(key)
	encrypted = box.encrypt(content) # ChaCha20-Poly1305 algorithm
	return encrypted

def ft_decrypt(user_key, encrypted):
	key = expand_key(user_key)
	box = SecretBox(key)
	content = box.decrypt(encrypted)
	return content