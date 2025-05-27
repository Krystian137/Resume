from flask import Flask, request, session
from flask_bootstrap import Bootstrap
from flask_babel import Babel

def get_locale():
    return session.get('lang', request.accept_languages.best_match(['en', 'pl']))

def create_app():
    app = Flask(__name__)

    app.secret_key = 'secret'

    Bootstrap(app)

    app.config['BABEL_DEFAULT_LOCALE'] = 'en'
    app.config['BABEL_SUPPORTED_LOCALES'] = ['en', 'pl']

    babel = Babel(app, locale_selector=get_locale)

    from routes import main
    app.register_blueprint(main)

    return app
