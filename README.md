# ClickBook - just choice the book

### Installation

WARNING!! (You need to have docker and docker-compose installed)

1. Create empty folder
1. There pass the command: `git clone https://github.com/lyf2000/clickbook.git`
1. In `Dockerfile` put your Google account credits
    ```dockerfile
    ENV EMAIL_HOST_USER <google email>
    ENV EMAIL_HOST_PASSWORD <password>
    ```
1. Run the following commands:
    ```
    docker build .
   # wait a time... bunch of inputs...
   docker-compose run web python /code/manage.py migrate
   ...
   docker-compose run web python /code/manage.py createsuperuser
   # here you've gotta to put credits to your superuser (username, email, password)
   ...
   docker-compose  up -d --build
    ```
1. There is! You just need to open `http://localhost:8000/admin/` page and create new books

### TUT

List of APIs:

- Registration `/signup/` POST body:
    ```
    {
       "username": "<new username>"  
       "password": "<your password>"  
    }
    ```
- Authorization. Here You're getting `access_token` which is gotta to be put in `Authorization` header `/login/` POST body:
    ```
    {
       "username": "<your username>"  
       "password": "<your password>"  
    }
    ```
- Books `/books/` GET you will get:
    ```
    [
      ...
      {
        "id": <int>,
        "name": <string>,
        "cost": <int>,
        "author": {
          "id": <int>,
          "fio": <string>
        }
      }
      ...
    ]
    ```
- Authors `/authors/` GET you will get:
    ```
    [
      ...
      {
        "id": <int>,
        "fio": <string>
        "books_count": <int>,
        "books": {
          "id": <int>,
          "name": <string>,
          "cost": <int>
        }
      }
      ...
    ]
    ```
- Order book. You need to have header `Authorization: Bearer <token>`. '/books/order/' POST  body:
    ```
    "book": <book id>,
    "call": <phone number int>,
    "comment": <string> # OPTIONAL
    ```
