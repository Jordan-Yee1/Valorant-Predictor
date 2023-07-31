import requests
from pymongo import MongoClient
import certifi
import pymongo
import ssl

connection = 'mongodb+srv://jordan:jyee@valorantinfo.bid9zc0.mongodb.net/'
client = MongoClient(connection,tlsCAFile=certifi.where())

db = client['Valorant_Matches']
collection = db['Results']


def get_match_results():
    url = 'https://vlrggapi.vercel.app/match/results'
    response = requests.get(url, headers={'accept': 'application/json'})

    if response.status_code == 200:
        data = response.json()
        # Process the data as needed
        results = data["data"]["segments"]

        for item in results:
            team_one = item["team1"]
            team_two = item["team2"]
            score_one = item["score1"]
            score_two = item["score2"]

            match_data = {
                "team_one": team_one,
                "team_two": team_two,
                "score_one": score_one,
                "score_two": score_two
            }

            print(f"Team One : {team_one} Score : {score_one} | Team Two : {team_two} Score : {score_two}")
    
            collection.insert_one(match_data)

    else:
        print(f'Request failed with status code {response.status_code}, response: {response.text}')
        return None


get_match_results()

client.close()
