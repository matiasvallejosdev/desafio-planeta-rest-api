# Introduction

PlanetChallengeAPI gives you fully control access to many endpoints to be accessed inside the video game. It has, pieces, slots, questions, answers and topics to handle the video game.

This documentation describes all the available API calls and properties of the returned objects. If you have any questions, please reach out to **contact@planetchallenge.com**

> At this time the bees-tat API is unstable. This means that the way it works and the data it returns may change at any time. Breaking changes are rare, but do happen. Proper versioning will be introduced in a future release.

# Understanding database

This database was designed to build a game. The objective is support the data necessary to build the game. It is not related to users.

The database has two purposes. First, it provides a list of topics and games that are necessary to build the game. Second, it provides all the necessary for the questions and answers. Each trivia was connected with a topic. Besides, each topic will be connected with a game that will save the images url, sprites and all metadata needed to start a new game.

Having said this, you should be able to identify the following entites necessary to build the database:

* Game
* Piece
* Topic
* Slot
* Trivia
* Question
* Type
* Answer

Now, the following diagram represent the logic relations between the entities and the set of minimal attributes of them. Take look at the diagram.

<img src="db/db-diagram.png" alt="db-design" style="max-width: 780px"/>

_Diagram developed in `diagrams.net` to represent the entity-relation model_

> Note: Database is developed for a video game. It will be divided following the game design and the requerimientos for the project [climate challenge](https://github.com/matiasvallejosdev/planet-challenge-game) game. Otherwise, it can be used for other purposes. 

# Getting Started

[`https://desafioplaneta.com/api/`](https://desafioplaneta.com/api/)

## Step 1 — Obtaining an API Key

The API credentials were stored inside each instance of the game and will be created only by a game.

> Only client games can obtain API key.

1. Use postman to get your `API_KEY` authentication token.

```bash
https://desafioplaneta.com/api/token/
```
### Step 2 — Setup

There are four properties that you must include in every API call.

1. `Authorization` A 40-character alphanumeric string that gives you access to use the API.

Take look at the header of the request:
```json
{
  "Authorization": "Token 13262sdh12ds1wwedj655"
}
```

> This is necessary to access to all restricted queries.

2. `method` An actions you can perform on a resource.
3. `arguments` JSON-encoded values sent to the method, sometimes optional.


## Step 3 — Test connection

With that in mind, the next step is to send a `POST` or `GET` request to `api.beestat.io` with the appropriate values set.

1. Set up your request headers with `Authorization` parameter
2. Use postman and send mock GET request to the following domain:

Test your API.

```bash
https://desafioplaneta.com/api/
```

## Step 4 — Run setup

1. You're good to go!

All API calls will return JSON a set of properties. Exceptions to this will be specified in the documentation.

> You should always attempt to JSON decode the response, then use the success property to determine if the API call succeeded.

# API Reference

## Open Endpoints

Open endpoints require no Authentication.

* [`POST /auth`](api/auth_api/post.md)
* [`GET /api`](api/base_api/get.md)

## Endpoints that require Authentication

Closed endpoints require a valid Token to be included in the header of the
request. A Token can be acquired from the Login view above.

* [`GET /user`](api/auth_api/get.md)
* [`GET /game`](api/game_api/get.md)
* [`GET /topic`](api/topic_api/get.md)
* [`GET /trivia`](api/trivia_api/get.md)

