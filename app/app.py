from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def index(name='home'):
	return 'Hello World! This is {}'.format(name)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port='8000')