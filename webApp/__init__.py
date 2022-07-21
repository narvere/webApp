from flask import Flask

# set FLASK_APP=webApp.py
# set FLASK_ENV=development
# flask run


def create_app():
   app = Flask(__name__) # создание приложения Flask

   app.config['SECRET_KEY'] = 'denisshohlov'
   app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

   from webApp.views.webApp import webApp as webApp_blueprint  # загрузка и регистрация блупринтов
   app.register_blueprint(webApp_blueprint)

   return app