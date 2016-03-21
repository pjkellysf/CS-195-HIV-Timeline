from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def index(name='home'):
	return render_template("index.html")

if __name__ == '__main__':
	#App can be rendered at -> localhost:5000 or 127.0.0.1:5000
	app.run(debug=True)