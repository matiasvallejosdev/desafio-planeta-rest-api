# API

API endpoint allow you to access to the documentation and to test the api connection using authentication keys. This is a public endpoint.

GET /api
---

This endpoint allow you to test your api connection using the authentication header requested.

**Arguments**

None required.

**Example Request**

```bash
GET https://desafioplaneta.com/api/?api_key={YOUR API KEY}
```

**Example Response**

[response_get_api.json](response/response_get_api.json)


GET /api/docs
--

This endpoint generates automatically an api documentation using [`drfdocs`](https://github.com/manosim/django-rest-framework-docs) third part application.

**Arguments**

None required.

**Example Request**

```bash
GET https://desafioplaneta.com/api/docs/
```

**Example Response**

Auto generated response documentation. Take look at the official generator [drfdocs](https://github.com/manosim/django-rest-framework-docs).