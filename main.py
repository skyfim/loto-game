from player import Player
import random

human = Player()
computer = Player()
barrels = []
sep = "-" * 5
for i in range(1, 91): barrels.append(i)

while True:
    new_barrel = random.choice(barrels)
    barrels.remove(new_barrel)
    print(f"Новый бочонок: {new_barrel}! (Осталось {len(barrels)}) ")
    print(f"{sep}Ваша карточка{sep}\n{human.sheet}")
    human.remove_number(new_barrel)

    if len(barrels) == 0:
        print("Игра окончена!")
        break


