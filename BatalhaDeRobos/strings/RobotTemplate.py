robot_art = r""" .
      0: {cabeça_name}
      ESTA DISPONIVEL: {cabeça_status}
      ATAQUE: {cabeça_attack}                              
      DEFESA: {cabeça_defense}
      CONSUMO DE ENERGIA: {cabeça_energy_consump}
                  ^
                  |                  |1: {arma_name}
                  |                  |ESTA DISPONIVEL: {arma_status}
                                     |ATAQUE: {arma_attack}
                             ------> |DEFESA: {arma_defense}
                _____                |CONSUMO DE ENERGIA: {arma_energy_consump}
               X_____\
       .-^-.  ||_| |_||  .-^-.
      /_\_/_\_|  |_|  |_/_\_/_\             |2: {braço_esquerdo_name}
      ||(_)| __\_____/__ |(_)||             |ESTA DISPONIVEL: {braço_esquerdo_status}
      \/| | |::|\```/|::| | |\/             |ATAQUE: {braço_esquerdo_attack}
      /`---_|::|-+-+-|::|_---'\             |DEFESA: {braço_esquerdo_defense}
     / /  \ |::|-|-|-|::| /  \ \            |CONSUMO DE ENERGIA: {braço_esquerdo_energy_consump}
    /_/   /|`--'-+-+-`--'|\   \_\  ----->   |  
    | \  / |===/_\ /_\===| \  / |           |3: {braço_direito_name}
    |  \/  /---/-/-\-\  o\  \/  |           |ESTA DISPONIVEL: {braço_direito_status}
    | ||| | O / /   \ \   | ||| |           |ATAQUE: {braço_direito_attack}
    | ||| ||-------------|o|||| |           |DEFESA: {braço_direito_defense}
    | ||| ||----\ | /----|o|||| |           |CONSUMO DE ENERGIA: {braço_direito_energy_consump}
    | _|| ||-----|||-----|o|||_ |    
    \/|\/  |     |||     |o|\/|\/    |4: {perna_esquerda_name}
    \_o/   |----|||||----|-' \o_/    |ESTA DISPONIVEL: {perna_esquerda_status}
           |##  |   |  ##|           |ATAQUE: {perna_esquerda_attack}
           |----|   |----|           |DEFESA: {perna_esquerda_defense}
           ||__ |   | __||           |CONSUMO DE ENERGIA: {perna_esquerda_energy_consump}
          [|'  `|] [|'  `|]  ---->   | 
          [|`--'|] [|`--'|]          |5: {perna_direita_name}
          /|__| |\ /| |__|\          |ESTA DISPONIVEL: {perna_direita_status}
          ||  | || ||    ||          |ATAQUE: {perna_direita_attack}
          ||__|_|| ||_|__||          |DEFESA: {perna_direita_defense}
          ||    || ||    ||          |CONSUMO DE ENERGIA: {perna_direita_energy_consump}
          \|----|/ \|----|/    
          /______\ /______\
          |__||__| |__||__|

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



