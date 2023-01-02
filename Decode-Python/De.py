import base64

def main():
    # Encode the string with base64
    encoded_string = base64.b64encode("Hallo world")

    # Print the encoded string
    print(encoded_string)

if __name__ == "__main__":
    main()
