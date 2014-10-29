from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/report_home')
def report_home():
	return render_template('report_home.html')

@app.route('/graph1')
def graph1():
	return render_template('graph1.html')

@app.route('/reports')
def reports():
	return render_template('reports.html')

@app.route('/report1')
def report1():
	return render_template('report1.html')

@app.route('/details')
def details():
	return render_template('details.html')

@app.route('/redcap_site')
def redcap_site():
	return render_template('redcap_site.html')

@app.route('/graph2')
def graph2():
	return render_template('graph2.html')

if __name__ == '__main__':
	app.run(debug=True)