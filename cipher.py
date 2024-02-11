def main():


    text = 'mrttaqrhknsw ih puggrur'
    custom_key = 'happycoding'

    text = input('What text would you like to encrypt/decrupt?\n')
    custom_key = input('What is the key?\n')
    direction = input('Do you wish to encrypt or decrypt your your message?\n')

    def vigenere(message, key, direction=1):
        key_index = 0
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        final_message = ''

        for char in message.lower():

            # Append any non-letter character to the message
            if not char.isalpha():
                final_message += char
            else:        
                # Find the right key character to encode/decode
                key_char = key[key_index % len(key)]
                key_index += 1

                # Define the offset and the encrypted/decrypted letter
                offset = alphabet.index(key_char)
                index = alphabet.find(char)
                new_index = (index + offset*direction) % len(alphabet)
                final_message += alphabet[new_index]
        
        return final_message

    def encrypt(message, key):
        return vigenere(message, key)
        
    def decrypt(message, key):
        return vigenere(message, key, -1)


    if direction == 'encrypt':
        print(f"You entered:\nText:{text}\nKey:{custom_key}\n Encryption iniitating....\n")
        entry = encrypt(text, custom_key)
        print(f"Encryption complete!\n You're new encrpted message is\n{entry}")
    else:
        print("You entered:\nText: {text}\nKey: {custom_key}\n Decryption iniitating....\n")
        entry = decrypt(text, custom_key)
        print(f"Decryption complete!\n You're decrypted  message is\n{entry}")

    

    # print(f'\nEncrypted text: {text}')
    # print(f'Key: {custom_key}')
    # decryption = decrypt(text, custom_key)
    # print(f'\nDecrypted text: {decryption}\n')

main()