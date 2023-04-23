from strings import Menus, RobotTemplate
from models import Robot
from utils import clean_scream, custom_sleep


from random import choice, randint

def build_robot(is_machine):
    
    if is_machine:
        robot_name = choice(RobotTemplate.names_robot)
        color_code = choose_color(True)
        robot = Robot(robot_name, color_code)
        robot.print_status()
        return robot
    else:
        robot_name = input("🎫| NOME DO ROBO:\n> ")
        color_code = choose_color(False)
        robot = Robot(robot_name, color_code)
        robot.print_status()
        return robot


def choose_color(is_machine):
    
    if is_machine:
        available_colors = RobotTemplate.colors
        print("ROBOT ESCOLHENDO A COR:")
        list_colors = RobotTemplate.colors.keys
        chosen_color = choice(list(RobotTemplate.colors.keys())) # cria uma lista com todas as chaves e escolhe uma cor aleatoria desta lista  
        color_code = available_colors[chosen_color]
        custom_sleep(2)
        clean_scream()
        return color_code
    else:
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
    print(Menus.tower_mode)
    print("🤖| DADOS DO JOGADOR 1:")
    robot_one = build_robot(False)
    custom_sleep(5)
    clean_scream()
    print("🤖| DADOS DO JOGADOR 2:")
    robot_two = build_robot(True)
    custom_sleep(5)
    clean_scream()
    current_robot = robot_one
    enemy_robot = robot_two
    rount = 0

    while playing:
        if rount % 2 == 0:
            current_robot = robot_one
            enemy_robot = robot_two
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
            clean_scream()
        else:
            current_robot = robot_two
            enemy_robot = robot_one
            current_robot.print_status()

            print("QUE PARTE DEVO USAR PARA ATACAR?:")
            part_to_use = randint(1,5)

            enemy_robot.print_status()
            print("QUAL PARTE DO INIMIGO DEVEMOS ATACAR?")
            part_to_attack = randint(1,5)

            current_robot.attack(enemy_robot, part_to_use, part_to_attack)
            rount += 1

            clean_scream()
        
        
        if not enemy_robot.is_on() or enemy_robot.is_there_available_part() == False:
            playing = False
            print(f"PARABÉNS, ROBO: {enemy_robot.name} VOCÊ GANHOU!!")
