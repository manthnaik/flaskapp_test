from flask import Flask
app = Flask(__name__)

@app.route('/')
def test1():
	print('Inside test1() method')
	return 'Accessed endpoint powered by Plask and Python'

@app.route('/param')
def param_home():
	print('Inside param_home() method')
	return 'Parameter may be submitted to this url.'

@app.route('/param/<name>')
def param_submit(name):
	print('Inside param_submit() method')
	return 'Parameter %s!' %name
	
if __name__=='__main__':
	app.run()


