#Ejercicio 21

plays = []
amount = int(input("Cuántas partidas querés ingresar? "))

for i in range(amount):
    print(f"Partida {i + 1}:")
    player1 = input("Jugada de Player 1 (R, P, S): ").strip().upper()
    player2 = input("Jugada de Player 2 (R, P, S): ").strip().upper()
    
    plays.append((player1, player2))


def win_plays(player1, player2):
    rules = {"R": "S", "S": "P", "P": "R"}

    if player1 == player2:
        return 0  
    elif rules[player1] == player2:
        return 1  
    else:
        return 2  

def total_win(plays):
    p1 = 0
    p2 = 0

    for player1, player2 in plays:
        result = win_plays(player1, player2)
        if result == 1:
            p1 += 1
        elif result == 2:
            p2 += 1

    if p1 > p2:
        return "Player 1"
    elif p2 > p1:
        return "Player 2"
    else:
        return "Tie"


result = total_win(plays)
print(f"Resultado Final: {result}")