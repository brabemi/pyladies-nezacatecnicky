import requests

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

cat_api = CatFacts()
dog_api = DogFacts()

print(cat_api.get_random_fact())
print(dog_api.get_random_fact())
