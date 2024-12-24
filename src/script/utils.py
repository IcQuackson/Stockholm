import os

def log(str):
	from stockholm import SILENT_ENABLED
	if not SILENT_ENABLED:
		print(str)

def rename_file(filename, new_filename):
	os.rename(filename, new_filename)

def load_extensions(path):
	with open(path, 'r') as file:
		return [f.strip() for f in file.readlines()]