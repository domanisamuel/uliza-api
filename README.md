# uliza-api
uliza is a stack overflow-like platform for questions and answers

- users endpoints
`POST /api/users` to add a user
`GET /api/users` to fetch all users
`GET /api/users/<int:id>` to fetch a specific / single user
`PUT /api/users/<int:id>'=`  to modify a user
`DELETE /api/users/<int:id>`  to delete a user

| Action| Endpoint | Functionality | 
|----------|----------|---------------|
| GET | `/api/users`  | Get all users|
| POST | `/api/users`  | add a user|
| GET | `/api/users/<int:id>`  | Get a single user|
| PUT | `/api/users/<int:id>`  | EDIT a user|
| DELETE | `/api/users/<int:id>`  | Delete a user|

### Prerequisites
Python3 (A programming language)
Flask (A Python microframework)
Virtualenv (Stores all dependencies used in the project)
Pivotal Tracker (A project management tool) (optional)
Pytest (Tool for testing)
The app is hosted on heroku

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