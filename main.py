from random import choices
from time import sleep
from os import system, name

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
How long would you like your password to be?

"""

def main():
    """A loop function that runs the program repeatedly."""
    try:
        while True:
            system("cls" if name == "nt" else "clear")
            mode = ""

            in_text = input(select_mode_text)

            for char in in_text.lower():
                if char in modes and char not in mode:
                    mode.join(char)

            if not mode:
                mode = "abcd"

            # chatgpt is sped
            avch = "".join([a if char == 'a' else b if char == 'b' else c if char == 'c' else d for char in mode])

            char_no_in = input(select_char_num_text)

            char_no = int(char_no_in) if char_no_in.isdigit() else 12

            password = "".join(choices(avch, k=char_no))

            print(f"\nThe password is:\n{password}")

            try:
                with open("password.md", "w") as f:
                    f.write(password)
                    print("Successfully written password to file. (./password.md)")
                    f.close()
            except Exception:
                print("Failed to Write to file.")

            print("Press Ctrl+C to exit.")
            sleep(15)
    
    except KeyboardInterrupt:
        exit()


if __name__ == "__main__":
    main()
