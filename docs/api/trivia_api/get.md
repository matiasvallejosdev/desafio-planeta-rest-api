# Trivia

A trivia endpoint you can get a set questions with answers. This set are consider each round of a topic. You usually will call it before the game starts.

GET /trivia
---

This endpoint gives you access to a list of all topics available in the game grouped by game.

**Auth required** : YES

**Permissions required** : `isAuthenticated`

**Arguments**

* `all`: List all or only published. **Optional**

**Example Request**

```bash
GET https://desafioplaneta.com/api/trivia/
```

**Example Response**

[response_get_game.json](responses/response_get_game.json)

GET /trivia/topic/`topic_id`
---

This endpoint gives you access to a list of trivias filtered by topic id. Each trivia object has a set of questions and answers.

**Auth required** : YES

**Permissions required** : `isAuthenticated`

**Arguments**

* `topic_id` - The ID of the topic. **Required**.
* `all`: List all or only published. **Optional**.

**Example Request**

```bash
GET https://desafioplaneta.com/api/trivia/<id>/
```

**Example Response**

[response_get_game-id.json](responses/response_get_trivias-by-topic-id.json)