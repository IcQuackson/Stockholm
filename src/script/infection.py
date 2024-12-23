
def infect(args):
	if args.silent:
		print("Silent mode enabled")
	if args.reverse:
		print("Reverse mode enabled")
	else:
		print("Infection mode enabled")
	print(f"Key: {args.key}")