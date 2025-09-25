### Setup
1. Make `.env` and paste values from `.env.dev`
2. `docker network create fastapi_interview_pet`
3. `docker compose up`
4. http://localhost:8000/docs#/


### Input data for Create/Update 'Users'
```json
{
  "gender": "female",
  "name": {
        "title": "Miss",
        "first": "Jennie",
        "last": "Nichols"
  },
  "location": {
    "street": {
      "number": 8929,
      "name": "Valwood Pkwy",
    },
    "city": "Billings",
    "state": "Michigan",
    "country": "United States",
    "postcode": "63104",
    "coordinates": {
      "latitude": "-69.8246",
      "longitude": "134.8719"
    },
    "timezone": {
      "offset": "+9:30",
      "description": "Adelaide, Darwin"
    }
  },
  "email": "jennie.nichols@example.com",
  "login": {
    "username": "yellowpeacock117",
    "password": "addison",
  },
  "dob": {
    "date": "1992-03-08T15:13:16.688Z",
    "age": 30
  },
  "phone": "(272) 790-0888",
  "cell": "(489) 330-2385",
}
```

### Input data for Create/Update 'Books'
```json
{
  "book_title": "The Great Gatsby",
  "short_description": "A classic novel about the American Dream",
  "description": "The story primarily concerns the young and mysterious millionaire Jay Gatsby and his quixotic passion for the beautiful Daisy Buchanan.",
  "public_date": "1925-04-10T00:00:00",
  "type": "FICTION",
}
```

### Input data for Create/Update 'Publisher'
```json
{
  "publisher_name": "Penguin Random House",
  "publisher_info": "One of the world's largest trade book publishers, formed by the merger of Penguin Group and Random House in 2013.",
  "publisher_status": "OPEN",
}
```