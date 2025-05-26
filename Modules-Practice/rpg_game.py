import random

def validate_number(word):
    while True:
        try:
            number = int(input(word))
            return number
        except ValueError:
            print("Please enter number only!")

def players_action():
    while True:
        action = validate_number("Please choose action (1-2)\n"
                                 "[1] Attack\n"
                                 "[2] Heal\n"
                                 "Action: ")
        if action == 1:
            print()
            return 1
        elif action == 2:
            print()
            return 2
        else:
            print("Please enter 1-2 only!")

def show_winner(player, monster, turn):
    if player > 0:
        print(f"Player won with {player} HP remaining in turn {turn}")
    elif monster > 0:
        print(f"Monster won with {monster} HP remaining in turn {turn}")
    else:
        print("TIED!")

def stats():
    random_attack = random.randint(1,5)
    random_heal = random.randint(1,5)

    return random_attack, random_heal

def player_turn(player_hp, monster_hp):
    print(f"Your HP: {player_hp} | Monster HP: {monster_hp}")
    random_attack, random_heal = stats()
    if players_action() == 1:
        monster_hp -= random_attack
        monster_hp = max(monster_hp, 0)
        print(f"You hit the monsters for {random_attack} damage!")
    else:
        player_hp += random_heal
        player_hp = min(player_hp, 20)
        print(f"You have healed {random_heal} of your HP")
    if random_attack == 5:
        random_attack *= 2
        print("⚡ Critical hit!")

    return player_hp, monster_hp

def monster_turn(player_hp, monster_hp):
    random_attack, random_heal = stats()
    if monster_hp > 12:
        random_action = 1
    else:
        random_action = random.randint(1, 2)

    if random_action == 1:
        player_hp -= random_attack
        player_hp = max(player_hp, 0)
        print(f"Monster attacks and hits you for {random_attack} damage!")
    else:
        monster_hp += random_heal
        monster_hp = min(monster_hp, 20)
        print(f"Monster have healed {random_heal} of their HP")
    if random_attack == 5:
        random_attack *= 2
        print("⚡ Critical hit!")
    return player_hp, monster_hp


def main():
    player_hp = 20
    monster_hp = 20
    turn = 0

    while player_hp > 0 and monster_hp > 0:
        player_hp, monster_hp = player_turn(player_hp, monster_hp)
        player_hp, monster_hp = monster_turn(player_hp, monster_hp)

        print()
        turn += 1

    show_winner(player_hp, monster_hp, turn)
main()