import flask
import os

app = flask.Flask(__name__)

@app.route('/')
def main():
    return flask.render_template('index.html', title="Astro Music Space")
    

if __name__ == '__main__':
    app.run()