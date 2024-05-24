n = int(input())
game = { 'STRAWBERRY': 0, 'BANANA': 0, 'LIME': 0, 'PLUM': 0 }
for _i in range(n):
    s, x = input().split()
    x = int(x)
    game[s] += x

must_hit_bell = False
for key in game:
    must_hit_bell = must_hit_bell or game[key] == 5

if must_hit_bell:
    print('YES')
else:
    print('NO')
