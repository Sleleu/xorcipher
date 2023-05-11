import argparse

def read_input(input_str):
    try:
        with open(input_str, 'r') as file:
            data = file.read().strip()
        return data
    except FileNotFoundError:
        return input_str

def encrypt(key, m):
	encrypted = ""
	for i in range(len(m)):
		c = ord(m[i])
		k = key[i % len(key)]
		encrypted += str(c ^ k) + " "
	return encrypted


def decrypt(key, c):
    decrypted = ""
    values = list(map(int, c.split()))
    for i in range(len(values)):
        c = values[i]
        k = key[i % len(key)]
        decrypted += chr(c ^ k)
    return decrypted

def main():
		
	parser = argparse.ArgumentParser()
	parser.add_argument("--encrypt", nargs=2, metavar=("key", "message"), help="Encrypt a message using XOR cipher")
	parser.add_argument("--decrypt", nargs=2, metavar=("key", "encrypted"), help="Decrypt an encrypted message using XOR cipher")
	args = parser.parse_args() 

	if args.encrypt:
		key_input = read_input(args.encrypt[0])
		message = read_input(args.encrypt[1])
		key = list(map(int, key_input.split()))
		encrypted = encrypt(key, message)
		print(encrypted)
	elif args.decrypt:
		key_input = read_input(args.decrypt[0])
		encrypted = read_input(args.decrypt[1])
		key = list(map(int, key_input.split()))
		decrypted = decrypt(key, encrypted)
		print(decrypted)
	else:
		parser.print_help()

if __name__ == "__main__":
    main()
