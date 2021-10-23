import random

class Code:
    """This class is responsible for generating and storing the secret code
    to be guessed by the players. This class is also responsible for checking
    and declaring if the code is guessed.

    Stereotype:
        Service Provider, Informtion Holder

    Attributes:
        _key (list of numbers): The secret code to be guessed by the players.
        _is_guessed (boolean): Determines if the code is already guessed or not.
    """

    def __init__(self):
        """Constructor for the Code class.

        Args:
            self (Code): An instance of Code.

        Returns:
            None.
        """
        self._key = []
        for _ in range(4):
            self._key.append(random.randint(1, 9))
        self._is_guessed = False

    def get_result(self, guess):
        """This method checks the player's guess against the secret code. Depending
        on the player's guess, they will receive a hint that can help them on their
        next guess.

        Args:
            self (Code): An instance of Code.
            guess (Guess): The player's guess.
        
        Returns:
            list of char: The hints for the player.
        """
        hint = []
        numbers = guess._get_numbers()

        if numbers == self._key:
            self._is_guessed = True
            hint = ["X", "X", "X", "X"]
        else:
            for i in range(len(self._key)):
                if numbers[i] == self._key[i]:
                    hint.append("X")
                elif numbers[i] in self._key:
                    hint.append("O")
                else:
                    hint.append("*")
        
        return hint

    def guessed(self):
        """This method returns the _is_guessed attribute.

        Args:
            self (Code): An instance of Code.
            
        Returns:
            boolean: Determines whether the player has guessed the secret code or not.
        """
        return self._is_guessed