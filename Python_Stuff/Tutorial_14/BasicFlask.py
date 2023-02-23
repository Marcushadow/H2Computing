import flask

app = flask.Flask(__name__)



@app.route('/')
def home():
    return "Routed to home directory"

@app.route("/NO")
def no():
    return "No"


if __name__ == '__main__':
    app.run()