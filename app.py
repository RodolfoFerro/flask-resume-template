import yaml
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    website_data = yaml.load(open('_config.yaml'))

    return render_template('index.html', data=website_data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
