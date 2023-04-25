robot_art = r"""
      0: {head_name}
      ESTA DISPONIVEL: {head_status}
      ATAQUE: {head_attack}                              
      DEFESA: {head_defense}
      CONSUMO DE ENERGIA: {head_energy_consump}
              ^
              |                  |1: {weapon_name}
              |                  |ESTA DISPONIVEL: {weapon_status}
     ____     |    ____          |ATAQUE: {weapon_attack}
    |oooo|  ____  |oooo| ------> |DEFESA: {weapon_defense}
    |oooo| '    ' |oooo|         |CONSUMO DE ENERGIA: {weapon_energy_consump}
    |oooo|/\_||_/\|oooo|          
    `----' / __ \  `----'           |2: {left_arm_name}
   '/  |#|/\/__\/\|#|  \'           |ESTA DISPONIVEL: {left_arm_status}
   /  \|#|| |/\| ||#|/  \           |ATAQUE: {left_arm_attack}
  / \_/|_|| |/\| ||_|\_/ \          |DEFESA: {left_arm_defense}
 |_\/    O\=----=/O    \/_|         |CONSUMO DE ENERGIA: {left_arm_energy_consump}
 <_>      |=\__/=|      <_> ------> |
 <_>      |------|      <_>         |3: {right_arm_name}
 | |   ___|======|___   | |         |ESTA DIPONIVEL: {right_arm_status}
// \\ / |O|======|O| \  //\\        |ATAQUE: {right_arm_attack}
|  |  | |O+------+O| |  |  |        |DEFESA: {right_arm_defense}
|\/|  \_+/        \+_/  |\/|        |CONSUMO DE ENERGIA: {right_arm_energy_consump}
\__/  _|||        |||_  \__/        
      | ||        || |          |4: {left_leg_name} 
     [==|]        [|==]         |ESTA DISPONIVEL: {left_leg_status}
     [===]        [===]         |ATAQUE: {left_leg_attack}
      >_<          >_<          |DEFESA: {left_leg_defense}
     || ||        || ||         |CONSUMO DE ENERGIA: {left_leg_energy_consump}
     || ||        || || ------> |
     || ||        || ||         |5: {right_leg_name}
   __|\_/|__    __|\_/|__       |ESTA DIPONIVEL: {right_leg_status}
  /___n_n___\  /___n_n___\      |ATAQUE: {right_leg_attack}
                                |DEFESA: {right_leg_defense}
                                |CONSUMO DE ENERGIA: {right_leg_energy_consump}
                                
"""

colors = {
    "Preto": '\x1b[90m',
    "Azul": '\x1b[94m',
    "Ciano": '\x1b[96m',
    "Verde": '\x1b[92m',
    "Magenta": '\x1b[95m',
    "Vermelho": '\x1b[91m',
    "Amarelo": '\x1b[93m',
}

names_robot = {
    1: "Magneto",
    2: "Apolo",
    3: "Hercules",
    4: "Zeus"
}



