from m import main
from flask import Flask, render_template, request
from flask.helpers import send_from_directory, send_from_directory
from flaskwebgui import FlaskUI
from stateClass import State
import os

app = Flask(__name__)
app._static_folder = os.path.abspath("static/")
ui = FlaskUI(app)

@app.route('/')
def stick():
    state = State()
    ma = main()
    state._init_("2020-presidential.csv", '10/6/2020')
    stateList = state.get_list()
    votes = ma.getVote(stateList)
    ma.operator(votes, stateList)
    status = ma.statusArr

    return render_template('index.html', status=status)


@app.route('/static/<path:filename>')
def serve_static(filename):
    root_dir = os.path.dirname(os.getcwd())
    return send_from_directory(os.path.join(root_dir, 'static', 'js'),   filename)

if __name__ == "__main__":

    ui.run()



