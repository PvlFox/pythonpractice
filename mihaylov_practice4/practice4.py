import urllib.request
import json
import random

class RickAndMortyClient:
    BASE_URL = "https://rickandmortyapi.com/api"

    def get_random_character(self):
        with urllib.request.urlopen(f"{self.BASE_URL}/character") as response:
            data = json.loads(response.read())
            return random.choice(data['results'])

    def search_characters(self, name: str):
        with urllib.request.urlopen(f"{self.BASE_URL}/character/?name={name}") as response:
            return json.loads(response.read())["results"]

    def get_all_locations(self):
        with urllib.request.urlopen(f"{self.BASE_URL}/location") as response:
            return json.loads(response.read())["results"]

    def search_episodes(self, name: str):
        with urllib.request.urlopen(f"{self.BASE_URL}/episode/?name={name}") as response:
            return json.loads(response.read())["results"]

client = RickAndMortyClient()
random_character = client.get_random_character()
print(f"Случайный персонаж: {random_character['name']}")