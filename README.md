
Travis CI
![](https://travis-ci.org/adelinetush/Yummy-Recipes.svg?branch=master) [![Coverage Status](https://coveralls.io/repos/github/adelinetush/Yummy-Recipes/badge.svg?branch=master)](https://coveralls.io/github/adelinetush/Yummy-Recipes?branch=master)  [![Maintainability](https://api.codeclimate.com/v1/badges/833e1712ca3af333c110/maintainability)](https://codeclimate.com/github/adelinetush/Yummy-Recipes/maintainability) 


# Yummy-Recipes

This application was built as part of the andela challenge. 

##### Project Url:
https://yummy-recipes-adeline.herokuapp.com/

##### Postman File:

[Postman file](https://github.com/adelinetush/Yummy-Recipes/tree/master/postman)

Technologies:

* Python (Flask web framework)

* PostgresDB

* Vanilla JS + JQuery

* HTML5/CSS

## Setup:

Install the dependencies for the application

 ```pip install -r requirements.txt```
 
### Database Migrations:

Intitiliaze the migrations folder in the root of the application

```python manage.py db init```

_This process is carried out once on install_

Add the migrated tables to the migration:

```python manage.py db migrate```

Update the database 

```python manage.py db upgrade```

#### FLASK API Documentation

* Login

*Authenticated:* false

*Endpoint:* _/auth/login_

*Method:* GET

*Variables:* email (string), password(string), username(string)

*Response:* ```Boolean(True,False)```

* Register

*Authenticated:* false

*Endpoint:* _/auth/register_

*Method:* GET

*Variables:* email (string), password(string)

*Response:* 
```
{
    "email": "adelinetush@gmail.com",
    "name": "andelatest",
    "password": "$6$rounds=656000$uQqrvkphjUUNYiDl$XM4Tl31pKdipuzZStV.dBYE8FkBVgoJRKNc4NV1Zc3ekKAJnQaLKgPnbvWL68OBEPsatZ/BViSKhdj4JY4/Im/"
}
```

 * Search

*Authenticated:* true

*Endpoint:* _/q_

*Method:* GET

*Variables:* name (string)

*Response:* 
```
[
    {
        "description": "The best damn dish in the world",
        "email": "adelinetush@gmail.com",
        "id": 1,
        "name": "Tuna Casserole"
    }
]
```

* Add Recipe

*Authenticated:* true

*Endpoint:* _/ar_

*Method:* POST

*Variables:* 

```
{
	"category":1,
	"name":"Tuna Casserole",
	"email":"adelinetush@gmail.com",
	"description":"The best damn dish in the world",
	"ingredients":[
		"1 pound of Tuna",
		"A bag of Flour"
	]
}
```

*Response:* 

```
[
	{
        "description": "The best damn dish in the world",
        "email": "adelinetush@gmail.com",
        "id": 1,
        "ingredients": "{\"1 pound of Tuna\",\"A bag of Flour\"}",
        "name": "Tuna Casserole"
    }
]
```
 * Get User Recipes

*Authenticated:* true

*Endpoint:* _/qu_

*Method:* GET

*Variables:* email (string)

*Response:* 

```
[
    {
        "description": "The best damn dish in the world",
        "email": "adelinetush@gmail.com",
        "id": 1,
        "ingredients": "{\"1 pound of Tuna\",\"A bag of Flour\"}",
        "name": "Tuna Casserole"
    }
]
```

 * Add Category

*Authenticated:* true

*Endpoint:* _/ac_

*Method:* POST

*Variables:* 

```
{
	"email":"adelinetush@gmail.com",
	"name":"Casseroles",
	"description":"A subset of awesome foods"
}
```

*Response:* 

```
[
    {
        "description": "A subset of awesome foods",
        "email": "adelinetush@gmail.com",
        "id": 1,
        "name": "Casseroles"
    }
]
```
* Get User Categories

*Authenticated:* true

*Endpoint:* _/guc_

*Method:* GET

*Variables:* name(string)

*Response:* 

```
[
    {
        "description": "A subset of awesome foods",
        "email": "adelinetush@gmail.com",
        "id": 1,
        "name": "Casseroles"
    }
]
```

* Get All Categories

*Authenticated:* true

*Endpoint:* _/gac_

*Method:* GET

*Variables:* none

*Response:* 

```
[
    {
        "description": "A subset of awesome foods",
        "email": "adelinetush@gmail.com",
        "id": 1,
        "name": "Casseroles"
    },
     {
        "description": "A subset of awesome foods",
        "email": "adelinetush@gmail.com",
        "id": 2,
        "name": "Pies"
    },
]
```

* Get Authentication Token

*Authenticated:* true

*Endpoint:* _/api/token_

*Method:* GET

*Variables:* username(string),password(string)

*Response:* 

```
{
    "duration": 600,
    "token": "eyJhbGciOiJIUzI1NiIsImlhdCI6MTUwOTY5NzY0MywiZXhwIjoxNTA5Njk4MjQzfQ.eyJpZCI6NH0.M3UUFpD1AhNrehgK_Hs4B7vIZFapgC13jIW6AybpNAw"
}

```

### Sample Headed API Calls

```
http://eyJhbGciOiJIUzI1NiIsImlhdCI6MTUwOTY5NzY0MywiZXhwIjoxNTA5Njk4MjQzfQ.eyJpZCI6NH0.M3UUFpD1AhNrehgK_Hs4B7vIZFapgC13jIW6AybpNAw@127.0.0.1:5000/api/resource
```


