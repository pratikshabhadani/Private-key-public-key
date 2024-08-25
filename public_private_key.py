def custom_hash(input_str):
    hash_value = 0
    prime = 31
    for char in input_str:
        hash_value = (hash_value * prime + ord(char)) % (10**10)
    return str(hash_value).zfill(10)

def generate_master_keys(private_key):
    master_private_key = private_key
    master_public_key = custom_hash(master_private_key)
    return master_private_key, master_public_key

def derive_child_public_key(master_private_key, index):
    combined_key = master_private_key + str(index)
    child_private_key = custom_hash(combined_key)
    child_public_key = custom_hash(child_private_key)
    return child_public_key

def verify_public_key(master_private_key, public_key, max_keys=50):
    for i in range(max_keys):
        if derive_child_public_key(master_private_key, i) == public_key:
            return True
    return False

def main():
    private_key = input("Enter your private key: ").strip()
    master_private_key, _ = generate_master_keys(private_key)

    max_keys = 50
    num_keys = int(input(f"How many public keys do you want to generate (1-{max_keys})? ").strip())
    
    public_keys = []
    for i in range(min(num_keys, max_keys)):
        public_key = derive_child_public_key(master_private_key, i)
        public_keys.append(public_key)
        print(f"Public Key {i}: {public_key}")

    while True:
        choice = input("Do you want to verify a public key? (yes/no): ").strip().lower()
        if choice == 'yes':
            public_key_to_verify = input("Enter the public key to verify: ").strip()
            is_valid = verify_public_key(master_private_key, public_key_to_verify, max_keys)
            if is_valid:
                print("The public key is valid.")
            else:
                print("The public key is not valid.")
        elif choice == 'no':
            print("Program terminated.")
            break
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    main()
