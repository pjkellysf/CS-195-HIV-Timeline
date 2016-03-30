from flask import Flask
from flask import render_template
import events
import csv

app = Flask(__name__)
db = events.createDb()

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/dbTesting')
def dbTesting():
	f = open('timeline.csv', encoding='utf-8')
	csv_f = csv.reader(f)
	string = []
	for row in csv_f:
  		string.append(row)

	return render_template('dbTesting.html', string=string)

if __name__ == '__main__':
	#App can be rendered at -> localhost:5000 or 127.0.0.1:5000
	app.run(debug=True)

