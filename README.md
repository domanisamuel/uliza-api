# uliza-api
uliza is a stack overflow-like platform for questions and answers

#### posts endpoints
| Action| Endpoint | Functionality | 
|----------|----------|---------------|
| GET | `/api/v1/posts`  | Get all posts|
| POST | `/api/v1/posts`  | add a post|
| GET | `/api/v1/posts/<int:post_id>`  | Get a single post|
| PUT | `/api/v1/posts/<int:post_id>`  | EDIT a post|
| DELETE | `/api/v1/posts/<int:post_id>`  | Delete a post|

- A `post` can either be a question or an answer, what differentiates them are `tags`

post schema:
```json

  {
    "post_id": 3,
    "tag": "question",
    "content":"What tech stack does Airbnb use?"
  }

```
```json
  {
    "post_id": 5,
    "tag": "answer",
    "content":"From what I know, they use React and Rails."
  }
```

#### users endpoints
| Action| Endpoint | Functionality | 
|----------|----------|---------------|
| GET | `/api/v1/users`  | Get all users|
| POST | `/api/v1/users`  | add a user|
| GET | `/api/v1/users/<int:user_id>`  | Get a single user|
| PUT | `/api/v1/users/<int:user_id>`  | EDIT a user|
| DELETE | `/api/v1/users/<int:user_id>`  | Delete a user|

user schema:
```json
  {
    "user_id":2,
    "firstname": "Eric",
    "lastname": "Omondi",
    "email":"eriko@bigtymz.comedy",
    "password":"cheka254"
  }

```

### Prerequisites
- Python3 (A programming language)
- Flask (A Python microframework)
- Virtualenv (Stores all dependencies used in the project)
- Pivotal Tracker (A project management tool) (optional)
- Pytest (Tool for testing)
- The app is hosted on heroku

### Getting Started:
Setting up the app locally.

Install pip:

`$ sudo apt-get install python-pip`

Clone this repository:

`$ git clone https://github.com/domanisamuel/uliza-api`

Get into the root directory:

`$ cd uliza-api/`

Install virtualenv:

`$ pip install virtualenv`

Create a virtual environment in the root directory:

`$ virtualenv -name of virtualenv-`

Note: If you do not have python3 installed globally, please run this command when creating a virtual environment:

`$ virtualenv -p python3 -name of virtualenv-`

Activate the virtualenv:

`$ source name of virtualenv/bin/activate`

Install the requirements of the project:

`$ pip install -r requirements.txt`

Create a file in the root directory called .env and add the two lines below

`export FLASK_APP="run.py"`

`export SECRET="some random string"`

Activate the env variables:

`$ source .env`

Run the application:

`$ python run.py`

To run tests:

`$ pytest`
