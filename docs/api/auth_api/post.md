# Auth

A login is the authentication system used in order to get the authentication token. Without token, you can't access to private data. That help you to protect your application.

POST /auth
---

This endpoint allow you to test your api connection using the authentication header requested.

**Arguments**

'None required.'

**Example Request**

```bash
GET https://desafioplaneta.com/api/auth/
```

**Example Response**

[response_get_api.json](responses/response_post_api-test.json)


POST /auth/token
---

This endpoint gives you an authorization through an authentication token given the user and password.

**Auth required** : NO

**Permissions required** : None

**Arguments**

* `email`: The user to authenticate. **Required**
* `password`: The password to authenticate. **Required**

**Example Request**

```bash
GET https://desafioplaneta.com/api/auth/token/
```

**Example Response**

[response_get_game.json](responses/response_post_login.json)
