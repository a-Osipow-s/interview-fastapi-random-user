### Setup
1. Make `.env` and paste values from `.env.dev`
2. `docker network create fastapi_interview_pet`
3. `docker compose up`

### http://localhost:8000/docs#/
### TODO: We need to make some CRUD for random users.
### Input structure for Create/Update
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

### Need to save this fields data.
#### For User Table.
'gender', 'first_name', 'last_name', 'title', 'email', 'username', 'password', 'age', 'phone', 'cell'.

#### For Location Table.
'city', 'state', 'country', 'timezone', 'postcode', 'street_name', 'street_number'