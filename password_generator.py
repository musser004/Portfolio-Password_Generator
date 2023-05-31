from random import choice, randint, shuffle
import pyperclip


class PasswordGenerator:

    # Initialize with full list of available letters, numbers and symbols

    def __init__(self):
        self.letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                        't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                        'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # Method to generate password from letters/numbers/symbols lists. Random.shuffle changes order

    def generate_password(self, pass_input, end):

        # Randomized selections picked from letters/symbols/numbers lists. Order of characters is then randomly shuffled

        password_list = [choice(self.letters) for _ in range(randint(8, 10))]
        password_list += [choice(self.symbols) for _ in range(randint(2, 4))]
        password_list += [choice(self.numbers) for _ in range(randint(2, 4))]
        shuffle(password_list)

        # Password string created. Password field cleared and password inserted. Password then printed to terminal,
        # copied to clipboard, and then returned

        password = "".join(password_list)
        pass_input.delete(0, end)
        pass_input.insert(0, password)
        pyperclip.copy(password)
        print(f"Your password is: {password}")
        return password
