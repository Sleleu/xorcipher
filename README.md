# XOR Cipher

This is a simple command-line tool for encrypting and decrypting messages using the XOR cipher algorithm.

The XOR cipher is a basic symmetric encryption technique that operates on binary data. It applies the XOR (exclusive OR) operation between each character of the message and the corresponding element of a key. The same key is used for both encryption and decryption.

## Usage

The program accepts two modes of operation - encryption and decryption - which can be selected using command-line arguments.

For encryption:

```sh
python3 xorcipher.py -e <key> <message>
```

For Decryption:

```sh
python3 xorcipher.py -d <key> <encrypted>
```
The key and message or encrypted text can either be strings or paths to text files. If a file path is provided, the program will attempt to read the key/message from the file.

The key should be a series of integers separated by spaces.

### Example

Let's assume that your key.txt is as follows:

```sh
1234 5678 9012 3456 7890 1234 5678 9012 3456 7890 1234 5678 2456 3245 1245 9011
```
 use the following command:
 
 ```sh
> python3 xorcipher.py --encrypt key.txt "Hello World ! " 
1178 5707 9048 3564 7869 1266 5753 9051 3570 7870 1206 5646 2489 3213
```

And decrypt:
```sh
> python3 xorcipher.py --d key.txt cipher.txt             
Hello World ! 
```
