import random
import sys
import os
import time

class BattleRPG:
    def __init__(self):
        self.player_hp = 100
        self.enemy_hp = 100
        self.player_attack = 20
        self.enemy_attack = 20

    def display_message(self, message, duration=1.5):
        os.system('clear' if os.name == 'posix' else 'cls')
        print(message)
        time.sleep(duration)

    def player_turn(self):
        self.display_message("Your HP: {}\nEnemy HP: {}".format(self.player_hp, self.enemy_hp))
        print("(1) ATTACK")
        print("(2) HEAL")
        print("(3) RUN")
        choice = input("Choose your action: ")
        if choice == '1':
            self.attack_enemy()
        elif choice == '2':
            self.heal_player()
        elif choice == '3':
            self.display_message("You ran away!")
            sys.exit()
        else:
            self.display_message("Invalid choice. Try again.")
            self.player_turn()

    def enemy_turn(self):
        self.display_message("Enemy attacks!")
        damage = random.randint(10, 30)
        self.player_hp -= damage
        if self.player_hp <= 0:
            self.game_over("You died!")
        else:
            self.display_message("Enemy dealt {} damage to you!".format(damage))

    def attack_enemy(self):
        damage = random.randint(10, 30)
        self.enemy_hp -= damage
        self.display_message("You attacked the enemy for {} damage!".format(damage))
        if self.enemy_hp <= 0:
            self.game_over("You win!")

    def heal_player(self):
        self.player_hp += 50
        if self.player_hp > 100:
            self.player_hp = 100
        self.display_message("You healed yourself for 50 HP!")

    def game_over(self, message):
        self.display_message(message)
        sys.exit()

    def start_battle(self):
        self.display_message("A fierce battle begins!")
        while True:
            self.player_turn()
            self.enemy_turn()

def main():
    game = BattleRPG()
    game.start_battle()

if __name__ == "__main__":
    main()