"""Program to convert a user input's into their requested notational system type."""

notational_systems = [
    "Binary",
    "Hexadecimal",
    "Decimal"
]

def convert_to():
    while True:
        # Neatly display the drop zone options to the user
        x = 0
        for system in notational_systems:
            x += 1
            print(str(x) + ". " + system)

        # Ask the user to choose a drop zone
        notational_system_choice = str(input("\nWhat notational system would you like to convert to?\n"))

        # Validate the user's choice
        if notational_system_choice not in notational_systems:
            print(
                "\n"
                + notational_system_choice
                + " is an invalid choice. Please choose a notational system from the list provided:\n"
            )
        else:
            return notational_system_choice

def convert_from(convert_to_choice):
    while True:
        # Neatly display the drop zone options to the user
        x = 0
        for system in notational_systems:
            x += 1
            print(str(x) + ". " + system)

        # Ask the user to choose a drop zone
        notational_system_choice = str(input("\nWhich notational system would you like to covert to " + convert_to_choice + "?\n"))

        # Validate the user's choice
        if notational_system_choice not in notational_systems:
            print(
                "\n"
                + notational_system_choice
                + " is an invalid choice. Please choose a notational system from the list provided:\n"
            )
        else:
            return "\nYou chose " + notational_system_choice + ", great choice!\n"


class Conversion:
    """
    Class containing all methods required to convert between different notational systems.
    """
    def __init__(self):
        pass

    def binary_to_hex(self, user_input):
        """
        Converts user's binary value to hexadecimal.
        """
        pass

    def binary_to_decimal(self, user_input):
        """
        Converts user's binary value to decimal.
        """
        pass

    def hex_to_binary(self, user_input):
        """
        Converts user's hexadecimal value to binary.
        """
        pass

    def hex_to_decimal(self, user_input):
        """
        Converts user's hexadecimal value to decimal.
        """
        pass

    def decimal_to_binary(self, user_input):
        """
        Converts user's decimal value to binary.
        """
        pass

    def decimal_to_hex(self, user_input):
        """
        Converts user's decimal value to hexadecimal.
        """
        pass


def main():
    """
    1. Asks the user which notational system they'd like to convert from
    2. Asks the user which notational system they'd like to convert to
    3. Passes their input to the correct function
    4. Returns the input in the requested notational system
    """
    convert_to_choice = convert_to()
    convert_from_choice = convert_from(convert_to_choice)


if __name__ == "__main__":
    main()
