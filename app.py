import os
from flask import Flask, url_for, redirect, render_template, request

import flask_admin as admin
import flask_login as login

from views import AdminIndexView
from user import User

# Create Flask application
app = Flask(__name__)

# Create dummy secrey key so we can use sessions
app.config['SECRET_KEY'] = '123456790'

# Initialize flask-login
def init_login():
    login_manager = login.LoginManager()
    login_manager.init_app(app)

    # Create user loader function
    @login_manager.user_loader
    def load_user(user_id):
        return User.get(user_id)

# Flask views
@app.route('/')
def index():
    return render_template('index.html')


# Initialize flask-login
init_login()

# Create admin
admin = admin.Admin(app, 'Example: Auth UserMixin', index_view=AdminIndexView(), base_template='my_master.html')

if __name__ == '__main__':
    app.run(debug=True)
