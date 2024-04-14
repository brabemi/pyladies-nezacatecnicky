import requests

class CatFacts():
    BASE_URL = 'https://cat-fact.herokuapp.com'

    def _get_random_verified_fact(self):
        r = requests.get(f'{self.BASE_URL}/facts/random', params={'amount': 10})
        data = r.json()
        for fact in data:
            if fact['status']['verified']:
                return fact['text']

    def get_random_fact(self):
        return self._get_random_verified_fact()

cat_api = CatFacts()

print(cat_api.get_random_fact())
