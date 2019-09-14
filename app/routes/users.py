from app import app
from controllers.users import get_users

@app.route('/api/users', methods=['GET'])
get_users()
