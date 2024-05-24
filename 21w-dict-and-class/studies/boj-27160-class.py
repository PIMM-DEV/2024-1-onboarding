class Game:
    def __init__(self):
        self.strawberry = 0
        self.banana = 0
        self.lime = 0
        self.plum = 0

    def add_fruit(self, name: str, value: int):
        if name == 'STRAWBERRY':
            self.strawberry += value
        elif name == 'BANANA':
            self.banana += value
        elif name == 'LIME':
            self.lime += value
        elif name == 'PLUM':
            self.plum += value

n = int(input())
game = Game()

for _i in range(n):
    s, x = input().split()
    x = int(x)
    game.add_fruit(s, x)

must_hit_bell = \
game.strawberry == 5 or \
game.banana == 5 or \
game.lime == 5 or \
game.plum == 5

if must_hit_bell:
    print('YES')
else:
    print('NO')
