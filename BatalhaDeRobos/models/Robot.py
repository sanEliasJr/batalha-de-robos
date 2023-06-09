from models.PartsRobot import Part
from strings import RobotTemplate

class Robot:
    def __init__(self, name, color_code):
        self.name = name
        self.color_code = color_code
        self.energy = 100
        self.parts = [
            Part("cabeça", attack_level=5, defense_level=10, energy_consumption=5),
            Part("arma", attack_level=15, defense_level=0, energy_consumption=10),
            Part("braço_esquerdo", attack_level=3, defense_level=20, energy_consumption=10),
            Part("braço_direito", attack_level=6, defense_level=20, energy_consumption=10),
            Part("perna_esquerda", attack_level=4, defense_level=20, energy_consumption=15),
            Part("perna_direita", attack_level=8, defense_level=20, energy_consumption=15),
        ]
    

    def print_status(self):
        print(self.color_code)
        str_robot = RobotTemplate.robot_art.format(**self.get_part_status())
        self.greet()
        self.print_energy()
        print(str_robot)
        print(RobotTemplate.colors["Preto"])
    

    def greet(self):
        print("MEU NOME É ", self.name)
    

    def print_energy(self):
        print(f"EU TENHO {self.energy}% DE ENERGIA")
        
        
    def get_part_status(self):
        part_status = {}
        for part in self.parts:
            status_dict = part.get_status_dict()
            part_status.update(status_dict)
        return part_status
      

    def is_there_available_part(self):
        for part in self.parts:
            if part.is_available():
                return True
        return False
    

    def is_on(self):
        return self.energy >= 0


    def attack(self, enemy_robot, part_to_use, part_to_attack):
        enemy_robot.parts[part_to_attack].reduce_edefense(self.parts[part_to_use].attack_level) 
        self.energy -= self.parts[part_to_use].energy_consumption
    