# Hello World! :)
import time

def main():
    """Prints 'Hello World' one letter at a time with a small delay"""

    message = "Hello World!"

    for letter in message:
        print(letter, end="", flush=True)
        time.sleep(.5)

if __name__ == "__main__":
    main()