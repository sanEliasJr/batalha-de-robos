from strings import Menus, RobotTemplate
from models import Robot
from utils import clean_scream, custom_sleep


from random import choice, randint


class Game:
    
    def build_robot(self, is_machine):

        if is_machine:
            robot_name = choice(RobotTemplate.names_robot)
            color_code = self.choose_color(True)
            robot = Robot(robot_name, color_code)
            robot.print_status()
            return robot
        else:
            robot_name = input("🎫| NOME DO ROBO:\n> ")
            color_code = self.choose_color(False)
            robot = Robot(robot_name, color_code)
            robot.print_status()
            return robot


    def choose_color(self, is_machine):

        if is_machine:
            available_colors = RobotTemplate.colors
            print("ROBOT ESCOLHENDO A COR:")
            list_colors = RobotTemplate.colors.keys
            chosen_color = choice(list(RobotTemplate.colors.keys())) # cria uma lista com todas as chaves e escolhe uma cor aleatoria desta lista  
            color_code = available_colors[chosen_color]
            #custom_sleep(2)
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
                #custom_sleep(2)
                clean_scream()
                
    def create_player(self, number_players = 2, is_machine = False):
        list_player = []
        for player in range(0,number_players):
            print(f"🤖| DADOS DO JOGADOR {player+1}:")
            list_player.append(self.build_robot(is_machine))
            #custom_sleep(5)
            clean_scream()
        return list_player # TODO: Tem que desmembrar a lista para capturar o jogador
    
    def playing (self,robot_one, robot_two):
        
        rount = 0
        playing = True
        winner = False
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
                    winner = True
                    print(f"PARABÉNS, ROBO: {enemy_robot.name} VOCÊ GANHOU!!")
                    return winner
        
            
    def play(self, mode):
        
        if mode == 1: #Jogador vs Maquina
            print(Menus.solo_mode)
            real_player = self.create_player(1)
            machine_player = self.create_player(1,True)
            current_robot = real_player[0]
            enemy_robot  = machine_player[0]
            self.playing(current_robot, enemy_robot)
            
        elif mode == 2: #Multiplayer
            print(Menus.multiplaye_mode)
            list_player = self.create_player()
            current_robot = list_player[0]
            enemy_robot = list_player[1]
            self.playing(current_robot, enemy_robot)
            
        elif mode == 3: # Torre
            print(Menus.tower_mode)
            list_real_player = self.create_player(1)
            current_robot = list_real_player[0]
            enemy_robot = self.create_player(len(RobotTemplate.names_robot.keys()), True)
            for playing in range(1, len(enemy_robot)):
                is_winner = self.playing(current_robot, enemy_robot[playing])
                if is_winner:
                    continue
                else:
                    break

            