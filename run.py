from flask import Flask
from flask_restful import Api
from config.routes import initialize_routes
from flask_mongoengine import MongoEngine
#from env_config import mongodb_host

app = Flask(__name__)
api = Api(app)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/gestao-de-ventiladores'
}

db = MongoEngine(app)
initialize_routes(api)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
