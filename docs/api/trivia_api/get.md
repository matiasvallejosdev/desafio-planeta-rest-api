# Trivia

A trivia endpoint you can get a set questions with answers. This set are consider each round of a topic. You usually will call it before the game starts.


GET /trivia/
---

This endpoint gives a set of questions and answers related to a topic.

**Auth required** : YES

**Permissions required** : `isAuthenticated`

**Arguments**

None required.

**Example Request**

```bash
GET https://desafioplaneta.com/api/trivia/?api_key={YOUR API KEY}&topic_id={YOUR TOPIC ID}
```

**Example Response**

[response_get_game.json](responses/response_get_trivia.json)


GET /trivia/`id`
---

This endpoint gives you access to a specific trivia game.

**Auth required** : YES

**Permissions required** : `isAuthenticated`

**Arguments**

* `trivia_id` - The ID of the game. **Required**.

**Example Request**

```bash
GET https://desafioplaneta.com/api/trivia/<id>/?api_key={YOUR API KEY}
```

**Example Response**

[response_get_game-id.json](responses/response_get_trivia-id.json)