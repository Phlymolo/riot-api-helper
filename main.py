import requests
import json


# Returns just the content
def get_from_riot_games_api(riot_api_key, endpoint):
    base_url = 'https://na1.api.riotgames.com'
    headers = {'X-Riot-Token': riot_api_key}
    return json.loads(requests.request('GET', base_url + endpoint, headers=headers).content)


# Returns the full response (ie, content, response headers, etc)
def get_from_riot_games_api_full_response(riot_api_key, endpoint):
    base_url = 'https://na1.api.riotgames.com'
    headers = {'X-Riot-Token': riot_api_key}
    return requests.request('GET', base_url + endpoint, headers=headers)


# Example usage
key = 'ABC123'
endpoint = '/lol/summoner/v4/summoners/by-name/Phlymolo'
response = get_from_riot_games_api(key, endpoint)
