# Auth

An auth provider provides the set of rules, models to authenticate and authorizate users. They inherit from django base model users and are bein used by the authentication system of djago.

GET /user/
---

This endpoint gives you access to all users avaiables in database.

**Auth required** : YES

**Permissions required** : `isAuthenticated`, `isAdminOnly`

**Arguments**

None required.

**Example Request**

```bash
GET https://desafioplaneta.com/api/auth/user/
```

**Example Response**

[response_get_game.json](responses/response_get_user-list.json)


GET /user/`<id>`
---

This endpoint gives you access to specific user.

**Auth required** : YES

**Permissions required** : `isAuthenticated`, `isAdminOnly`

**Arguments**

None required.

**Example Request**

```bash
GET https://desafioplaneta.com/api/auth/user/<id>/
```

**Example Response**

[response_get_game.json](responses/response_get_user-pk.json)

