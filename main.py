import base64
import qrcode

def main():
    text = input("Enter text to encode: ")      # Takes user input
    text_base64 = encode(text)                  # Send value of "text" to encode function
    decode(text_base64)                         # Send value of text_base64 to decode function

def encode(text):
    text_bytes = text.encode("ascii")           # Encodes string of text into bytes
    text_base64 = base64.b64encode(text_bytes)  # Encodes bytes into base64
    print(f"Encoded text: {text_base64}")       # Prints encoded with base64
    return text_base64                          # Return value of text_base64

def decode(text_base64):
    decoded_text = base64.b64decode(text_base64)# Decodes base64 to bytes
    decoded_text = decoded_text.decode("ascii") # Decodes text from bytes to string
    print(f"Decoded text: {decoded_text}")      # Prints decoded text
    return decoded_text                         # Return decoded text

main()                                          # Calls main function, starting the program

