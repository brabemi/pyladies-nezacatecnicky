# Intro to API

## Co je to API

- Úvod do API - https://cojeapi.cz/01-uvod-do-api.html
- Klient vs server - https://cojeapi.cz/02-klient-server.html#
- Základní pojmy - https://cojeapi.cz/03-zakladni-pojmy.html

## Hrátky s API

API: https://alexwohlbruck.github.io/cat-facts/docs/endpoints/facts.html

### Browser

Plugin RESTED - https://chromewebstore.google.com/detail/rested/eelcnbccaccipfolokglfhhmapdchbfg?pli=1

Úkoly:
- Získejte jeden náhodný fakt o kočkách
- Získejte 25 náhodných faktů v jednom API call
- Zjistěte co říká fact s ID `5c609945e549020014533037`
- V jednom API call stáhněte fakta s ID:
  - `5a4aab2c2c99ee00219e11c4`
  - `5c609945e549020014533037`
  - `591f98783b90f7150a19c199`

Řešení:
- Získejte jeden náhodný fakt o kočkách - API obsahuje hromadu nepěkných dat
```
GET https://cat-fact.herokuapp.com/facts/random

{
  "status": {
    "verified": null,
    "sentCount": 0
  },
  "_id": "61a6493a6ce64cdd6328d295",
  "user": "61a622996ce64cdd6328ad91",
  "text": "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).",
  "type": "cat",
  "deleted": false,
  "createdAt": "2021-11-30T15:54:34.298Z",
  "updatedAt": "2021-11-30T15:54:34.298Z",
  "__v": 0
}
```
- Získejte 10 náhodných faktů v jednom API call
```
GET https://cat-fact.herokuapp.com/facts/random?amount=10

[
  {
    "status": {
      "verified": null,
      "sentCount": 0
    },
    "_id": "65ad103f2976af79f38cbcea",
    "user": "65a10ce7ae41a9d2cca4f2e2",
    "text": "А что мы знаем про котов.",
    "type": "cat",
    "deleted": false,
    "createdAt": "2024-01-21T12:38:23.020Z",
    "updatedAt": "2024-01-21T12:38:23.020Z",
    "__v": 0
  },
  {
    "status": {
      "verified": null,
      "sentCount": 0
    },
    "_id": "659d2184cb446c662b28fbf1",
    "user": "6597f8bf22b133ae60b194ec",
    "text": "Ааааааааа.",
    "type": "cat",
    "deleted": false,
    "createdAt": "2024-01-09T10:35:48.915Z",
    "updatedAt": "2024-01-09T10:35:48.915Z",
    "__v": 0
  },
  {
    "status": {
      "verified": null,
      "sentCount": 0
    },
    "_id": "65dcf3b721b2da182e05e710",
    "user": "65c2b64f93cb7a97849d2fd9",
    "text": "Cats have tiny hooks on their tongues, which feel like sandpaper, to help them clean and untangle their fur. Cats have tiny hooks on their tongues, which feel like sandpaper, to help them clean and untangle their fur. Cats have tiny hooks on their tongues, which feel like sandpaper, to help them clean and untangle their fur. Cats have tiny hooks on their tongues, which feel like sandpaper, to help them clean and untangle their fur. Cats have tiny hooks on their tongues, which feel like sandpaper, to help them clean and untangle their fur. Cats have tiny hooks on their tongues, which feel like sandpaper, to help them clean and untangle their fur. Cats have tiny hooks on their tongues, which feel like sandpaper, to help them clean and untangle their fur.",
    "type": "cat",
    "deleted": false,
    "createdAt": "2024-02-26T20:25:27.263Z",
    "updatedAt": "2024-02-26T20:25:27.263Z",
    "__v": 0
  },
  {
    "status": {
      "verified": null,
      "sentCount": 0
    },
    "_id": "63dbaf0b2b393f8bf4bb6cea",
    "user": "63d2405e6321d18c83b2b6f1",
    "text": "Ааа.",
    "type": "cat",
    "deleted": false,
    "createdAt": "2023-02-02T12:39:39.343Z",
    "updatedAt": "2023-02-02T12:39:39.343Z",
    "__v": 0
  },
  {
    "status": {
      "verified": null,
      "sentCount": 0
    },
    "_id": "62fd1c6455c657b3ac03bdf4",
    "user": "62f924d6294858641b12c7ef",
    "text": "Cats are one of, if not the most, popular pet in the world.",
    "type": "cat",
    "deleted": false,
    "createdAt": "2022-08-17T16:50:44.938Z",
    "updatedAt": "2022-08-17T16:50:44.938Z",
    "__v": 0
  },
  {
    "status": {
      "verified": null,
      "sentCount": 0
    },
    "_id": "64a9e478d8025fcd1384b860",
    "user": "649a8687e846b1eb98f70b7f",
    "text": "                                      .",
    "type": "cat",
    "deleted": false,
    "createdAt": "2023-07-08T22:34:32.955Z",
    "updatedAt": "2023-07-08T22:34:32.955Z",
    "__v": 0
  },
  {
    "status": {
      "verified": true,
      "sentCount": 1
    },
    "_id": "5ad9f10f734d1d2de1f501de",
    "updatedAt": "2020-08-23T20:20:01.611Z",
    "createdAt": "2018-04-19T01:10:54.673Z",
    "sendDate": "2018-04-20T20:20:00.673Z",
    "user": "5a9ac18c7478810ea6c06381",
    "text": "Exposing cats and dogs to marijuana can help reduce the suffering from a chronic and painful illness.",
    "deleted": false,
    "source": "user",
    "type": "cat",
    "used": false
  },
  {
    "status": {
      "verified": null,
      "sentCount": 0
    },
    "_id": "6419b25c58ed542f4eb91f8f",
    "user": "640399e77ef7aa816f4aae12",
    "text": "Лошади не спят.",
    "type": "cat",
    "deleted": false,
    "createdAt": "2023-03-21T13:34:20.053Z",
    "updatedAt": "2023-03-21T13:34:20.053Z",
    "__v": 0
  },
  {
    "status": {
      "verified": null,
      "sentCount": 0
    },
    "_id": "64ad7ad39cef901292225342",
    "user": "61b11802f9c77cdad2d21bd3",
    "text": "Horses fact.",
    "type": "cat",
    "deleted": false,
    "createdAt": "2023-07-11T15:52:51.508Z",
    "updatedAt": "2023-07-11T15:52:51.508Z",
    "__v": 0
  },
  {
    "status": {
      "verified": null,
      "sentCount": 0
    },
    "_id": "63c6fdb8220958920a6ffddc",
    "user": "63c4f77fa34280a8adddea15",
    "text": "Thntjm.",
    "type": "cat",
    "deleted": false,
    "createdAt": "2023-01-17T19:57:44.717Z",
    "updatedAt": "2023-01-17T19:57:44.717Z",
    "__v": 0
  }
]
```
- Zjistěte co říká fakta s ID:
  - `5a4aab2c2c99ee00219e11c4`
  - `5c609945e549020014533037`
  - `591f98783b90f7150a19c199`
```
GET https://cat-fact.herokuapp.com/facts/5a4aab2c2c99ee00219e11c4
{
  "status": {
    "verified": true,
    "sentCount": 1
  },
  "_id": "5a4aab2c2c99ee00219e11c4",
  "updatedAt": "2020-08-23T20:20:01.611Z",
  "createdAt": "2018-02-09T21:20:03.152Z",
  "user": {
    "name": {
      "first": "Alex",
      "last": "Wohlbruck"
    },
    "_id": "5a9ac18c7478810ea6c06381",
    "photo": "https://lh3.googleusercontent.com/a/ACg8ocJDXN6nxC9SDuxWqEpuFQTmqzjGD1J-TnV5zbAJ3yiPWxPO=s50"
  },
  "text": "Hearing is the strongest of cat's senses: They can hear sounds as high as 64 kHz — compared with humans, who can hear only as high as 20 kHz.",
  "deleted": false,
  "source": "user",
  "__v": 0,
  "type": "cat",
  "used": false
}

GET https://cat-fact.herokuapp.com/facts/5c609945e549020014533037
{
  "status": {
    "verified": true,
    "sentCount": 1
  },
  "_id": "5c609945e549020014533037",
  "updatedAt": "2020-08-23T20:20:01.611Z",
  "createdAt": "2019-02-10T21:36:05.210Z",
  "user": {
    "name": {
      "first": "Alex",
      "last": "Wohlbruck"
    },
    "_id": "5a9ac18c7478810ea6c06381",
    "photo": "https://lh3.googleusercontent.com/a/ACg8ocJDXN6nxC9SDuxWqEpuFQTmqzjGD1J-TnV5zbAJ3yiPWxPO=s50"
  },
  "text": "Do you ever wake up in the middle of the night and find your cat sleeping on your head? Cat behavioral experts believe that cats are drawn to the warmth and the familiar scent of the owner. Resting on your head also keeps kitty safe from your arms and legs if you toss and turn through the night.",
  "deleted": false,
  "type": "cat",
  "source": "user",
  "__v": 0,
  "used": false
}

GET https://cat-fact.herokuapp.com/facts/591f98783b90f7150a19c199
{
  "status": {
    "verified": true,
    "sentCount": 1
  },
  "_id": "591f98783b90f7150a19c199",
  "__v": 0,
  "text": "Cats sleep 16 to 18 hours per day. When cats are asleep, they are still alert to incoming stimuli. If you poke the tail of a sleeping cat, it will respond accordingly.",
  "source": "api",
  "updatedAt": "2020-08-23T20:20:01.611Z",
  "type": "cat",
  "createdAt": "2018-04-22T20:20:01.917Z",
  "deleted": false,
  "used": false,
  "user": {
    "name": {
      "first": "Alex",
      "last": "Wohlbruck"
    },
    "_id": "5a9ac18c7478810ea6c06381",
    "photo": "https://lh3.googleusercontent.com/a/ACg8ocJDXN6nxC9SDuxWqEpuFQTmqzjGD1J-TnV5zbAJ3yiPWxPO=s50"
  }
}
```

### Python requests

Requests: HTTP for Humans - https://requests.readthedocs.io/en/latest/

## Ostatní

https://github.com/public-apis/public-apis
