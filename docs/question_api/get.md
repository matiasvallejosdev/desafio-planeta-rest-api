# Questions

A questions individual questions that contain a set of answers assigned. They be usually query before each trivia round session.


GET /question
---

This endpoint gives you access to all questions. They can be filtered by `trivia_id`.

**Arguments**

None required.

**Example Request**

```bash
GET https://desafioplaneta.com/api/question/?trivia_id={YOUR TRIVIA ID}&api_key={YOUR API KEY}
```

**Example Response**

[response_get_game.json](responses/response_get_question.json)


GET /game/`<id>`
---

This endpoint gives you access to a specific game available from its ID.

**Arguments**

* `game_id` - The ID of the game. **Required**.

**Example Request**

```bash
GET https://desafioplaneta.com/api/game/<id>/?api_key={YOUR API KEY}
```

**Example Response**

[response_get_game-id.json](responses/response_get_game-id.json)
