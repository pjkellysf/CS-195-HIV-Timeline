from flask import Flask
from flask import render_template

app = Flask(__name__)
db = events.initialize()

@app.route('/')
def index():
	return render_template("index.html")

if __name__ == '__main__':
	#App can be rendered at -> localhost:5000 or 127.0.0.1:5000
	app.run(debug=True)

