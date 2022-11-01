import json
from pathlib import Path

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main_page():
    path = Path(f'{Path.home()}/cv/data.json')
    with open(path) as data:
        return render_template('index.html', **json.load(data))


if __name__ == '__main__':
    app.run()
