import requests

def get_match_results():
    url = 'https://vlrggapi.vercel.app/match/results'
    response = requests.get(url, headers={'accept': 'application/json'})

    if response.status_code == 200:
        return response.json()
    else:
        print(f'Request failed with status code {response.status_code}, response: {response.text}')
        return None

match_results = get_match_results()
if match_results:
    print(match_results)
else:
    print('Unable to fetch match results')
