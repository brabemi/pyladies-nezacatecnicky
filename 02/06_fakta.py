import requests
from random import choice

class CatFacts():
    BASE_URL = 'https://cat-fact.herokuapp.com'

    def _get_random_verified_fact(self):
        for attempt in range(10):
            r = requests.get(f'{self.BASE_URL}/facts/random', params={'amount': 10})
            data = r.json()
            for fact in data:
                if fact['status']['verified']:
                    return fact['text']
        raise Exception('We are out of facts about cats')

    def get_random_fact(self):
        return self._get_random_verified_fact()

class DogFacts():
    BASE_URL = 'https://dogapi.dog'

    def get_random_fact(self):
        r = requests.get(f'{self.BASE_URL}/api/facts')
        data = r.json()
        return data["facts"][0]

class NumberFacts():
    BASE_URL = 'http://numbersapi.com'

    def get_random_fact(self):
        r = requests.get(f'{self.BASE_URL}/random/trivia', params={'json': True})
        data = r.json()
        return data['text']

cat_api = CatFacts()
dog_api = DogFacts()
number_api = NumberFacts()

# print(cat_api.get_random_fact())
# print(dog_api.get_random_fact())
# print(number_api.get_random_fact())

while True:
    print('Copak by tě zajímalo, zadej "kocka", "pes", "cislo" nebo "nahoda" prřípadně "konec"')
    volba = input('Chci slyšet další fakt o: ')
    volba = volba.lower().strip()
    if volba in ["kocka", "kočka", "kocky", "kočky"]:
        print('Fakt o kočkách:', cat_api.get_random_fact())
    elif volba in ["pes", "psi"]:
        print('Fakt psech:', dog_api.get_random_fact())
    elif volba in ["cislo", "číslo", "cisla", "čísla"]:
        print('Fakt o číslech:', number_api.get_random_fact())
    elif volba in ["nahoda", "náhoda"]:
        random_api = choice([cat_api, dog_api, number_api])
        print('Náhodný fakt:', random_api.get_random_fact())
    elif volba in ["konec"]:
        break
    else:
        print(f'Volbu "{volba}" neznám')

print("Na viděnou příště")
