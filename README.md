# Run server
```sh
git clone https://github.com/xiaolibuzai-ovo/CreatifyHomeWork.git
cd CreatifyHomeWork
docker-compose up --build
```


# example

## signup
```sh
curl --location 'http://127.0.0.1:8000/signup/' \
    --header 'Content-Type: application/json' \
    --data-raw '{
        "email": "test@test.com",
        "password": "123"
    }'
```
### response
```json
{"id":1,"email":"test@test.com"}
```

## signin

```sh
curl --location 'http://127.0.0.1:8000/signin/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "email": "test@test.com",
    "password": "123"
}'
```

### responese
```json
{"access_token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJleHAiOjE3MTc3NDgyOTh9.tLgMC14CY9oagF8bXHhX1bXZtqccUjuIKx87kAboRMk","refresh_token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJleHAiOjE3MTc3NDgyOTh9.tLgMC14CY9oagF8bXHhX1bXZtqccUjuIKx87kAboRMk"}
```

## me
```sh
curl --location 'http://127.0.0.1:8000/me/' \
--header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJleHAiOjE3MTc3NDgyOTh9.tLgMC14CY9oagF8bXHhX1bXZtqccUjuIKx87kAboRMk'
```

### response
```json
{"id":1,"email":"test@test.com"}
```
