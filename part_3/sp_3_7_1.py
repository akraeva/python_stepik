result = {}


def new_card(command):
    result[command] = {'games': 0, 'win': 0, 'loos': 0, 'draw': 0, 'points': 0}
# {games:<всего игр> win:<побед> loos:<проигрышей> draw:<ничья> points:<очков>}


def card_update(command, own_score, opponent_score):
    command['games'] += 1
    if own_score > opponent_score:
        command['win'] += 1
        command['points'] += 3
    elif own_score == opponent_score:
        command['draw'] += 1
        command['points'] += 1
    else:
        command['loos'] += 1


def card_output(command):
    game = command['games']
    win = command['win']
    draw = command['draw']
    loos = command['loos']
    points = command['points']
    return (f'{game} {win} {draw} {loos} {points}')


n = int(input())  # кол-во матчей
for i in range(n):
    # формат ввода : 1команда;Забито_1командой;2команда;Забито_2командой
    command1, points1, command2, points2 = input().split(';')

    if command1 not in result:
        new_card(command1)
    if command2 not in result:
        new_card(command2)
    card_update(result[command1], int(points1), int(points2))
    card_update(result[command2], int(points2), int(points1))

for i in result:
    print(f'{i}:{card_output(result[i])}')
