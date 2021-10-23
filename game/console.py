class Console:
    """This class is responsible for reading inputs, writing prompts, and creating
    the interface of the Mastermind program.

    Stereotype: Service Provider, Interfacer

    Attributes:
    """

    def display(self, players):
        """Displays the current state of the game by printing the players and their
        corresponding guesses and hints.

        Args: 
            self (Console): An instance of Console.
            players (list of Players): The list of players where all of the data will
                be taken from.

        Returns:
            None
        """
        print("---------------------------------")
        for p in players:
            print(f"Player {p.get_name()}: ", end="")
            for n in p.get_guess()._get_numbers():
                print(n, end="")
            print(", ", end="")
            for h in p.get_hint():
                print(h, end="")
            print()
        print("---------------------------------")

    def read(self, prompt):
        """Prints a prompt that asks the user for a string/char input.
        
        Args:
            self (Console): An instance of Console.
            prompt (String): The prompt that identifies which string/char input is expected.

        Returns:
            String: The user's input in string/char format.
        """
        return input(prompt)

    def read_number(self, prompt):
        """Prints a prompt that asks the user for an integer input.

        Args:
            self (Console): An instance of Console.
            prompt (String): The prompt that identifies which int input is expected.
            
        Returns:
            Integer: The user's input in int format.
        """
        return int(input(prompt))

    def write(self, text):
        """Prints the passed text on the screen.

        Args:
            self (Console): An instance of Console.
            text (String): The text to be displayed.

        Returns:
            None.
        """
        print(text)
