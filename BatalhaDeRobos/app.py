from views import *
from models import Robot

from os import system
from time import sleep

    
def clean_scream():
    system('clear') or None


def build_robot():
    robot_name = input("🎫| Robot name: ")
    color_code = choose_color()
    robot = Robot(robot_name, color_code)
    robot.print_status()
    return robot


def choose_color():
    available_colors = RobotTemplate.colors
    chosen_color_valid = True
    while (chosen_color_valid):
        print("Available colors:")
        for key, value in available_colors.items():
            print(value, key)
        print(RobotTemplate.colors["White"])
        chosen_color = input("Choose a color: ").capitalize()
        if available_colors.get(chosen_color):
            color_code = available_colors[chosen_color]
            chosen_color_valid = False
            return color_code
        print("Codigo invalido!\nEspere para uma nova tentativa")
        sleep(2)
        clean_scream()


def play():

    print(Menus.main_menu)
    playing = True
    print("Welcome to the game!")
    print("🤖| Datas for player 1:")
    robot_one = build_robot()
    sleep(5)
    clean_scream()
    print("🤖| Datas for player 2:")
    robot_two = build_robot()
    sleep(5)
    clean_scream()
    current_robot = robot_one
    enemy_robot = robot_two
    rount = 0

    while playing:
        if rount % 2 == 0:
            current_robot = robot_one
            enemy_robot = robot_two
        else:
            current_robot = robot_two
            enemy_robot = robot_one
        current_robot.print_status()

        print("What part should I use to attack?:")
        part_to_use = input("Choose a number part: ")
        part_to_use = int(part_to_use)

        enemy_robot.print_status()
        print("Which part of the enemy should we attack?")
        part_to_attack = input("Choose a enemy number part to attack: ")
        part_to_attack = int(part_to_attack)

        current_robot.attack(enemy_robot, part_to_use, part_to_attack)
        rount += 1
        sleep(5)
        clean_scream()
        if not enemy_robot.is_on() or enemy_robot.is_there_available_part() == False:
            playing = False
            print(f"Congratulations, player: {enemy_robot.name}")
            sleep(5)
            clean_scream()

play()
