from flask import Flask, request
application = Flask(__name__)

@application.route("/")
def hello():
    return "Moooooooii!"

if __name__ == "__main__":
    application.run()
