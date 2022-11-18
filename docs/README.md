# Introduction


ClimateChallengeAPI gives you fully control access to many endpoints to be accessed inside the video game. It has, pieces, slots, questions, answers and topics to handle the video game.

This documentation describes all the available API calls and properties of the returned objects. If you have any questions, please reach out to **contact@desafioplaneta.com**

> At this time the bees-tat API is unstable. This means that the way it works and the data it returns may change at any time. Breaking changes are rare, but do happen. Proper versioning will be introduced in a future release.

# Getting Started

[`https://desafioplaneta.com/api/`](https://desafioplaneta.com/api/)

## Step 1 — Obtaining an API Key

The API credentials were stored inside each instance of the game and will be created only by a game.

> Only client games can obtain API key.

1. Use postman to get your `API_KEY` authentication token.

```bash
https://desafioplaneta.com/api/login/
```

## Step 2 — Test connection

There are four properties that you must include in every API call.

1. `api_key` A 40-character alphanumeric string that gives you access to use the API.
2. `method` An actions you can perform on a resource.
3. `arguments` JSON-encoded values sent to the method, sometimes optional.

With that in mind, the next step is to send a `POST` or `GET` request to `api.beestat.io` with the appropriate values set.

1. Use postman and send mock GET request to the following domain:

```bash
https://desafioplaneta.com/api/?api_key={YOUR API KEY}
```

## Step 3 — Run setup

1. You're good to go!

All API calls will return JSON with both a `success` and a `data` property. Exceptions to this will be specified in the documentation.

> You should always attempt to JSON decode the response, then use the success property to determine if the API call succeeded.

# API Reference

## Open Endpoints

Open endpoints require no Authentication.

* [`POST /login`](auth_api/post.md)
* [`GET /api`](base_api/get.md)

## Endpoints that require Authentication

Closed endpoints require a valid Token to be included in the header of the
request. A Token can be acquired from the Login view above.

* [`GET /game`](game_api/get.md)
* [`GET /trivia`](trivia_api/get.md)
* [`GET /topic`](topic_api/get.md)
* [`GET /question`](question_api/get.md)

