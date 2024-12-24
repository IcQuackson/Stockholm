
def log(str):
	from stockholm import SILENT_ENABLED
	if not SILENT_ENABLED:
		print(str)
