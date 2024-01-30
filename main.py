# Specifikācija
# - 1pt Spelētāji sāk no lauciņa nr. 1, vispār 100 lauciņu. Ir divi spēlētāji. Vinē tas kurš pirmais sasniedz pēdējo lauciņu
# - 1pt Maksimāli - 25 raundi, ja beidzas raundi - neizšķirts
# - 1pt Viens pēc otra met kauliņu (ar nejauša ciparu ģenerātora palidzību) un iet uz priekšu
# - 1pt Ja trāpa uz lauciņu ar kāpnem:
# -- zilas kāpnes ved uz leju, 18 -> 7, 67 -> 46 , 80 -> 69, 74 -> 63
# -- sarkanas kāpnes ved uz augšu, 15 -> 24, 39 -> 48, 33 -> 52, 87 -> 96 
# - 1pt Katrā raundā tik drukāta informācija kur atrodas spēlētājs, dators un vai ir uzkāpts uz kāpnem

# Koda vertēšanas kritēriji
# - 1pt Kodā izmanto mainīgus, ciklus (for vai while), zarošanu (if)
# - 1pt Kods strādā bez kļūdam
# - 1pt Mainīgo un funkciju nosaukumi atspoguļo izmantošanas būtību, bez saisinājumiem, rakstīti snake_case stilā
# - 1pt Kodam ir jēdzīgi komentāri, pirms "if, for" koda konstrukcijam
# - 1pt Izmaiņas saglabātas versiju vadības sistēmā Git

# Dokumentācija
# Mainīgie - https://www.w3schools.com/python/python_variables.asp
# Operācijas ar mainīgiem - https://www.w3schools.com/python/python_operators.asp
# Mainīgo drukāšana - https://www.w3schools.com/python/python_variables_output.asp
# Nosacījumi, zarošana, if ... else - https://www.w3schools.com/python/python_conditions.asp
# For cikls - https://www.w3schools.com/python/python_for_loops.asp
# Nejauša skaitļa generēšana - https://www.w3schools.com/python/ref_random_randint.asp
# Github Fork (repozitorija kopija) - https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo
# Klonēt repozitoriju - hhttps://code.visualstudio.com/docs/sourcecontrol/intro-to-git

import random

player_1 = 1
player_2 = 1

def check_ladders(location, player_type):
    # blue ladders
    # 18 -> 7, 67 -> 46 , 80 -> 69, 74 -> 63
    if location == 18:
        location = 7
        print(player_type, "on blue ladders, location", location)
    elif location == 67:
        location = 46
        print(player_type, "on blue ladders, location", location)
    elif location == 80:
        location = 69
        print(player_type, "on blue ladders, location", location)
    elif location == 74:
        location = 63
        print(player_type, "on blue ladders, location", location)
    
    # red ladders
    # 15 -> 24, 39 -> 48, 33 -> 52, 87 -> 96 
    if location == 15:
        location = 24
        print(player_type, "on red ladders, location", location)
    elif location == 39:
        location = 48
        print(player_type, "on red ladders, location", location)
    elif location == 33:
        location = 52
        print(player_type, "on red ladders, location", location)
    elif location == 87:
        location = 96
        print(player_type, "on red ladders, location", location)
    return location

# 25 rounds of game
for round in range(25):
    print("============")
    print("Round:", round)

    # throwing dice
    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1, 6)
    print("Player dice: " + str(dice_1) + " computer dice: " + str(dice_2))

    # moving players
    player_1 = player_1 + dice_1
    player_2 = player_2 + dice_2
    print("Player position: " + str(player_1) + " computer position: " + str(player_2))

    # check winners
    if player_1 >= 100:
        print("Player 1 won")
        break
    elif player_2 >= 100:
        print("Player 2 won")
        break

    # check ladders
    player_1 = check_ladders(player_1, "player")
    player_2 = check_ladders(player_2, "computer")

if player_1 != 100 and player_2 != 100:
    print("It's a tie")
