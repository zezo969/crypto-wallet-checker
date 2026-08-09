def check_wallet(address):
    if address.startswith("0x") and len(address) == 42:
        return "Valid EVM wallet format"
    return "Invalid wallet format"


wallet = input("Enter wallet address: ")
print(check_wallet(wallet))
