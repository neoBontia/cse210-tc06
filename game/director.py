from game.code import Code
from game.console import Console
from game.player import Player
from game.roster import Roster
from game.guess import Guess

class Director:
    def __init__(self):
        self._code = Code()
        self._console = Console()
        self._roster = Roster()
        self._keep_playing = True

    def start_game(self):
        self.prepare_game()

        while self._keep_playing:
            self.get_inputs()
            self.update()
            self.output()

    def prepare_game(self):
        for n in range(2):
            name = self._console.read(f"Enter a name for player {n + 1}: ")
            player = Player(name)
            self._roster.add_player(player)

    def get_inputs(self):
        players = self._roster.get_players()
        self._console.display(players)

        player = self._roster.get_current()
        self._console.write(f"{player.get_name()}'s turn:")
        guess = Guess(self._console.read_number("What is your guess? "))
        player.set_guess(guess)

    def update(self):
        player = self._roster.get_current()
        guess = player.get_guess()
        hint = self._code.get_result(guess)
        #print(hint)
        player.update_hint(hint)

    def output(self):
        if self._code.guessed():
            winner = self._roster.get_current()
            name = winner.get_name()
            print(f"\n{name} won!")
            self._keep_playing = False
        self._roster.next_player()