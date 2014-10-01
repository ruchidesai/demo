from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/alerts')
def alerts():
	return render_template('alerts.html')

@app.route('/details')
def details():
	return render_template('details.html')

@app.route('/errors')
def errors():
	return render_template('errors.html')

@app.route('/summary')
def summary():
	return render_template('summary.html')

@app.route('/graph1')
def graph1():
	return render_template('graph1.html')

if __name__ == '__main__':
	app.run(debug=True)