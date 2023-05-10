def main():
        
    key_str = input("Enter key values : ")
    key = list(map(int, key_str.split()))

    message = input("Enter text to encrypt : ")
    encrypted = ""

    for i in range(len(message)):
        c = ord(message[i])
        k = key[i % len(key)]
        encrypted += str(c ^ k) + " "
    
    print(f"key : {key}")
    print(f"Message : {message}")
    print("Encrypted message :", {encrypted})

if __name__ == "__main__":
    main()
