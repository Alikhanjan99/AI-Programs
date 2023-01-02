import base64

def main():
    # Encode the string with base64
    encoded_string = base64.b64encode("Hallo world")

    # Decode the encoded string to a string
    decoded_string = encoded_string.decode()

    # Print the decoded string
    print(decoded_string)

if __name__ == "__main__":
    main()
