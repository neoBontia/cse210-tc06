class Guess:
    """A guess from a player in the game. Responsility of Guess is to hold the guess from a player.

    Stereotype: 
        Information Holder

    Attributes:
        _numbers (list) : List of numbers.
    """

    def __init__(self):
        """The class constructor.

        Args:
            self (Guess): an instance of Guess.
        """
        self._numbers = []

    def _to_list(self, number):
        """Appends a number to the list

        Args:
            self (Guess): an instance of Guess.
            number (int): an integer
        """
        self._numbers.append(number)

    def _get_numbers(self):
        """Returns the list of numbers.

        Args:
            self (Guess): an instance of Guess.
        """
        return self._numbers
