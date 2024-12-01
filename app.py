from flask import Flask, render_template
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from auth import auth_blueprint 

# Inicializando as extensões fora da app
db = SQLAlchemy()
bcrypt = Bcrypt()
mail = Mail()

def create_app():
    app = Flask(__name__)

    # Configurações do app
    app.config['SECRET_KEY'] = 'sua_chave_secreta'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  

    # Inicializando as extensões
    db.init_app(app)
    bcrypt.init_app(app)
    mail.init_app(app)

    # Registrando o Blueprint de autenticação
    app.register_blueprint(auth_blueprint, url_prefix='/auth') 

    # Registrando a rota Home
    @app.route('/')
    def home():
        return render_template('home.html')  

    # Criar o banco de dados
    with app.app_context():
        db.create_all()  

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
