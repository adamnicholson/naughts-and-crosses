

class Board:
    positions = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    winners = [
        [1,2,3],
        [4,5,6],
        [7,8,9],
        [1,4,7],
        [2,5,8],
        [3,6,9],
        [1,5,9],
        [3,5,7],
    ]

    def __init__(self):
        self.used = {}

    def move(self, player, pos):
        self.used[int(pos)] = int(player)

    def available(self):
        free = []
        for pos in self.positions:
            if pos not in self.used.keys():
                free.append(pos)

        return free

    def winner(self):
        for player in [1, 2]:
            owned = []
            for pos in self.used.keys():
                if self.used[pos] == player:
                    owned.append(pos)

            for combination in self.winners:
                matched = 0
                for pos in combination:
                    if pos in owned:
                        matched += 1

                if matched == 3:
                    return player

        return None

    def iswinner(self, player: int):
        if self.won() and self.winner() == player:
            return True
        else:
            return False

    def won(self):
        return self.winner() is not None

    # The game is considered "over" if somebody has won, or there are no moves left
    def over(self):
        return self.winner() or not self.available()

    def whoseTurn(self):
        player1turns = 0
        player2turns = 0
        for pos in self.used.keys():
            if self.used[pos] == 1:
                player1turns += 1
            else:
                player2turns += 1

        return 2 if player2turns < player1turns else 1

    def isTurn(self, player: int):
        return self.whoseTurn() == player