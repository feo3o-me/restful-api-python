from flask import Flask
from acc import blueprint

flask_app = Flask(__name__)
flask_app.config["SERVER_NAME"] = "{}:{}".format('localhost', 1234)
flask_app.register_blueprint(blueprint)

if __name__ == '__main__':
    flask_app.run(debug=True)