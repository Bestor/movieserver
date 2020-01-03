POST

```
curl -X POST http://localhost:8000/api/movies/ -H "Content-Type: application/json" -d '{"title": "sharknado", "format": "s", "length": 62, "year": 2010, "rating": 1}'
{"title": "sharknado", "format": "s", "length": 62, "year": 2010, "rating": 1}
```

GET

```
~ » curl -X GET http://localhost:8000/api/movies/                   dalejo@btidevcustom
[{"title": "Lord of the Rings", "format": "d", "length": 160, "year": 2001, "rating": 5}, {"title": "Fight Club", "format": "v", "length": 154, "year": 1998, "rating": 4}]
```
