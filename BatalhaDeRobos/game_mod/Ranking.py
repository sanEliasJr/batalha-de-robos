from models import Ranking
from utils import format_date
from strings import Menus

def show ():
    print(Menus.ranking_menu)
    ranking = Ranking()
    response = ranking.getRanking()
    response_winner_list = response.json()
    for i in response_winner_list:
        print(f"({i['id']})   | {i['name']}   | {format_date(i['dataEvent'])}")
    