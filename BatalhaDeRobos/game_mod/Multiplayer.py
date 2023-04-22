from strings import *
from models import Robot
from utils import clean_scream, custom_sleep

def build_robot():
    robot_name = input("🎫| NOME DO ROBO:\n> ")
    color_code = choose_color()
    robot = Robot(robot_name, color_code)
    robot.print_status()
    return robot


def choose_color():
    available_colors = RobotTemplate.colors
    chosen_color_valid = True
    while (chosen_color_valid):
        print("CORES DISPONIVEIS:")
        for key, value in available_colors.items():
            print(value, key)
        print(RobotTemplate.colors["White"])
        chosen_color = input("ESCOLHA UMA COR PARA SEU ROBO:\n> ").capitalize()
        if available_colors.get(chosen_color):
            color_code = available_colors[chosen_color]
            chosen_color_valid = False
            return color_code
        print("CODIGO INVALIDO!\nESPERE UMA NOVA TENTATIVA")
        custom_sleep(2)
        clean_scream()


def play():

    playing = True
    print("Welcome to the game!")
    print("🤖| DADOS DO JOGADOR 1:")
    robot_one = build_robot()
    custom_sleep(5)
    clean_scream()
    print("🤖| DADOS DO JOGADOR 2:")
    robot_two = build_robot()
    custom_sleep(5)
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

        print("QUE PARTE DEVO USAR PARA ATACAR?:")
        part_to_use = input("ESCOLHA UM NUMERO DA PARTE DO ROBO:\n> ")
        part_to_use = int(part_to_use)

        enemy_robot.print_status()
        print("QUAL PARTE DO INIMIGO DEVEMOS ATACAR?")
        part_to_attack = input("ESCOLHA UM PARTE DO NUMERO INIMIGO PARA ATACAR:\n> ")
        part_to_attack = int(part_to_attack)

        current_robot.attack(enemy_robot, part_to_use, part_to_attack)
        rount += 1
        custom_sleep(5)
        clean_scream()
        if not enemy_robot.is_on() or enemy_robot.is_there_available_part() == False:
            playing = False
            print(f"PARABÉNS, ROBO: {enemy_robot.name} VOCÊ GANHOU!!")
            custom_sleep(5)
            
                
        clean_scream()


