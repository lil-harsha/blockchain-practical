import hashlib

def main():
    message = "Blockchain Developer"
    digest_hex = hashlib.sha256(message.encode("utf-8")).hexdigest()

    print("Message:", message)
    print("SHA-256 Digest (hex):", digest_hex)

if __name__ == "__main__":
    main()
