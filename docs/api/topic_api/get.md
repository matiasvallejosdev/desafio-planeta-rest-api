# Topic

A topic is a set of educational questions, answers and game that will help to build a game. You usually get it at the menu of the game.

GET /topic
---

This endpoint gives you access to a list of all topics available.

**Auth required** : YES

**Permissions required** : `isAuthenticated`

**Arguments**

* `all`: List all or only published. **Optional**

**Example Request**

```bash
GET https://desafioplaneta.com/api/topic/
```

**Example Response**

[response_get_game.json](responses/response_get_topic.json)


GET /topic/`<id>`
---

This endpoint gives you access to a specific topic available from its ID.

**Auth required** : YES

**Permissions required** : `isAuthenticated`

**Arguments**

* `topic_id` - The ID of the topic. **Required**.

**Example Request**

```bash
GET https://desafioplaneta.com/api/topic/<id>/
```

**Example Response**

[response_get_game-id.json](responses/response_get_topic-id.json)