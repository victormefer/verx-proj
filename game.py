import random


class Player:
    def __init__(self, name):
        self.name = name
        self.balance = 300
        self.position = 0
        self.properties = []
        self.lost = False


class Property:
    def __init__(self, cost, rent):
        self.cost = cost
        self.rent = rent
        self.owner = None


class Game:
    def __init__(self):
        self.players = []
        self.board = []

    def run_game(self):
        self.board = [
            Property(100, 10),
            Property(200, 20),
            Property(300, 25),
            Property(150, 15),
            Property(200, 40),
            Property(500, 50),
            Property(600, 60),
            Property(800, 80),
            Property(100, 15),
            Property(250, 25),
            Property(100, 10),
            Property(200, 20),
            Property(300, 25),
            Property(150, 15),
            Property(200, 40),
            Property(500, 50),
            Property(600, 60),
            Property(800, 80),
            Property(100, 15),
            Property(250, 25),
        ]

        player_names = ["impulsivo", "exigente", "cauteloso", "aleatorio"]

        for p in player_names:
            self.players.append(Player(p))

        for i in range(1000):
            for p in self.players:
                if p.lost:
                    continue

                dice = random.randint(1, 6)
                p.position += dice
                if p.position >= len(self.board):
                    p.position -= len(self.board)
                    p.balance += 100

                current_property = self.board[p.position]

                if current_property.owner is not None:
                    p.balance -= current_property.rent
                    current_property.owner.balance += current_property.rent
                    if p.balance < 0:
                        end_game = self.lose_player(p)
                        if end_game:
                            return self.end_game()
                elif current_property.cost <= p.balance:
                    if self.is_player_buying(p, current_property):
                        p.properties.append(current_property)
                        current_property.owner = p

        return self.end_game()

    def is_player_buying(self, player, current_property):
        if player.name == "impulsivo":
            return True
        elif player.name == "exigente":
            return current_property.rent >= 50
        elif player.name == "cauteloso":
            return player.balance - current_property.cost >= 80
        elif player.name == "aleatorio":
            return random.randint(0, 1)

    def lose_player(self, player):
        for p in player.properties:
            p.owner = None
        player.lost = True

        if [p.lost for p in self.players].count(False) == 1:
            return True
        return None

    def end_game(self):
        self.players.sort(reverse=True, key=lambda x: x.balance)
        return {
            "vencedor": self.players[0].name,
            "jogadores": [p.name for p in self.players]
        }