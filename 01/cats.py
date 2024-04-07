import requests

BASE_URL = 'https://cat-fact.herokuapp.com'

# 1 random fakt
def get_random_v1():
    r = requests.get(f'{BASE_URL}/facts/random')
    data = r.json()
    return data['text']

# Více faktů
def get_random_v2(amount=1):
    r = requests.get(f'{BASE_URL}/facts/random', params={'amount': amount})
    data = r.json()
    result = []
    for fact in data:
        result.append(fact['text'])
    return result

# Více faktů, filtr na ověřené
def get_random_v3(amount=1, verified=True):
    r = requests.get(f'{BASE_URL}/facts/random', params={'amount': amount})
    data = r.json()
    result = []
    for fact in data:
        if fact['status']['verified']:
            result.append(fact['text'])
    return result

# Fakta s daným ID
def get_by_ids(ids):
    result = {}
    for id in ids:
        r = requests.get(f'{BASE_URL}/facts/{id}')
        data = r.json()
        result[id] = (data['text'])
    return result

print(get_random_v1())
print(get_random_v2(amount=10))
print(get_random_v3(amount=100))

cat_ids = [
  '5a4aab2c2c99ee00219e11c4',
  '5c609945e549020014533037',
  '591f98783b90f7150a19c199',
]

print(get_by_ids(cat_ids))
