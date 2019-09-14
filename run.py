from app import app
from flask import jsonify

# import models
from app.models.users import users_db
# remeber users_db is a fuction in the models so we pass the returned values to users
users = users_db()

@app.route('/')
def get_users():
    return jsonify({
        'users': users
    })
if __name__  ==   "__main__":
    app.run(debug=True)