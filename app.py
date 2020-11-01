from flask import Flask, render_template, request
from test import test

app = Flask(__name__)
app._static_folder = '/Users/gabrielwersebe/Desktop/Coding/Group/US-Presidential-Election-2020/static'

@app.route('/')
def stick():
    t = test()
    status = test.statusArr
    return render_template('index.html', status=status)

if __name__ == "__main__":
    app.run()



