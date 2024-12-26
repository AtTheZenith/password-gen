from random import choice
from time import sleep

modes = "abcd"
a = "abcdefghijklmnopqrstuvwxyz"
b = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
c = "1234567890"
d = "`~!@#$%^&*()-=_+[]{};:,./<>?|"

select_mode_text = f"""
Select text to use for the password:
a. {a}
b. {b}
c. {c}
d. {d}

Example:
    Selecting 'ab' will give capital and lowercase letters.
    Selecting 'c' will only give numbers.
    Selecting 'abcd' will give letters, numbers, and symbols.

"""

select_char_num_text = """
How many characters would you like to have?

"""

def main():
    """A loop function that runs the program repeatedly."""
    try:
        while True:
            mode = ""
            avch = ""

            in_text = input(select_mode_text)

            for char in in_text.lower():
                if char in modes and char not in mode:
                    mode += char

            if mode == "":
                mode = "abcd"

            for char in mode:
                if char == "a":
                    avch += a
                elif char == "b":
                    avch += b
                elif char == "c":
                    avch += c
                elif char == "d":
                    avch += d

            char_no_in = input(select_char_num_text)

            char_no = char_no_in.isdigit() and int(char_no_in) or 12

            password = ""
            for _ in range(char_no):
                password += choice(avch)

            print(f'The password is:\n{password}\n(Press Ctrl+C to exit.)')
            sleep(15)
    
    except KeyboardInterrupt:
        exit()


if __name__ == "__main__":
    main()
