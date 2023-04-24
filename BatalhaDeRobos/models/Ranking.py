import requests

class Ranking():

    url = 'https://6441b15a33997d3ef900bc0a.mockapi.io/api/v1/Winner'


    def getRanking(self):
       response= requests.get(self.url)
       return response 

    def postRanking(self, name, date):
        data = {
            "name": name,
            "dataEvent": date
        }
        response = requests.post(self.url, data)
        return response




