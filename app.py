import oyaml as yaml
from flask import Flask
from flask import render_template

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


@app.route('/')
def index():
    website_data = yaml.load(open('_config.yaml'), Loader=yaml.FullLoader)

    return render_template('index.html', data=website_data)


if __name__ == '__main__':
    app.run(debug=False, port=5000)
