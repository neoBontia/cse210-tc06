class Player:
    """A person taking part in a game. Responsility of Player is to give a guess.

    Stereotype: 
        Information Holder

    Attributes:
        _name (string): The player's name.
        _guess (Guess): The player's guess.
        _hint (list) : The player's hint.
    """

    def __init__(self, name):
        """The class constructor.

        Args:
            self (Player): an instance of Player.
        """
        self._name = name
        self._guess = None
        self._hint = []

    def get_guess(self):
        """Returns the player's last guess (an instance of Guess). If the player 
        hasn't guessed yet this method returns None.

        Args:
            self (Player): an instance of Player.
        """
        return self._guess

    def get_name(self):
        """Returns the player's name.

        Args:
            self (Player): an instance of Player.
        """
        return self._name

    def get_hint(self):
        """Returns the player's hint.

        Args:
            self (Player): an instance of Player.
        """
        return self._hint

    def set_guess(self, guess):
        """Sets the player's last move to the given instance of Guess.

        Args:
            self (Player): an instance of Player.
            guess (Guess): an instance of Guess
        """
        self._move = guess

    def update_hint(self, hint):
        """Updates the player's hint.

        Args:
            self (Player): an instance of Player.
            hint (list): a list 
        """
        self._hint = hint
