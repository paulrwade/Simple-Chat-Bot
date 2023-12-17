hero_damage = 100


def double_damage():
    global hero_damage
    hero_damage = hero_damage * 2


def disarmed():
    global hero_damage
    hero_damage = hero_damage * .1


def power_potion():
    global hero_damage
    hero_damage += 100


count_to_number = int(input())
current_number = 0

while current_number <= count_to_number:
    print(current_number)
    current_number += 1         #increment by 1