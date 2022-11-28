# API

API endpoint allow you to access to the documentation of the REST api.

GET /api/
--

This endpoint allows you to test your api connection and credentials.

**Auth required** : YES

**Permissions required** : `isAuthenticated`, `isAdminOnly`

**Arguments**

None required.

**Example Request**

```bash
GET https://desafioplaneta.com/api/
```

**Example Response**

[response_get_game.json](responses/response_get_api.json)

GET /api/docs
--

This endpoint generates automatically an api documentation using [`drfdocs`](https://github.com/manosim/django-rest-framework-docs) third part application.

**Auth required** : NO

**Permissions required** : `isAuthenticated`, `isAdminOnly`

**Arguments**

None required.

**Example Request**

```bash
GET https://desafioplaneta.com/api/docs/
```

**Example Response**

Auto generated response documentation. Take look at the official generator [drfdocs](https://github.com/manosim/django-rest-framework-docs).