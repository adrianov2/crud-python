from flask import Blueprint, render_template

auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@auth_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html')

@auth_blueprint.route('/home')
def home():
    return render_template('home.html')  

@auth_blueprint.route('/reset_password')
def reset_password():
    return render_template('reset_password.html')  

@auth_blueprint.route('/profile')
def profile():
    return render_template('profile.html')  
