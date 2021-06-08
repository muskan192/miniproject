from flask import Flask, render_template, url_for, request
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = '66d8e8e4010865c69f12897f71e93afd'




@app.route("/")

@app.route("/home")
def home():
	return render_template('home.html', methods=['GET', 'POST'])

@app.route("/landbot")
def landbot():
	return render_template('landbot.html',title='landbot')

@app.route("/profile")
def profile():	
	return render_template('profile.html',title='profile')

@app.route("/login")
def login():
	return render_template('login.html',title='login')

@app.route("/admin", methods=['GET', 'POST'])
def admin():
    return render_template('admin.html', title='Admin')

@app.route("/feedback")
def feedback():
	return render_template('feedback.html',title='feedback')

@app.route("/orderlog")
def orderlog():
	return render_template('orderlog.html',title='orderlog')

@app.route("/contactlog")
def contactlog():
	return render_template('contactlog.html',title='contactlog')

@app.route('/contact')
def contact():
    return render_template('contact.html', title='contact')

@app.route('/contactt')
def contactt():
    return render_template('contactt.html', title='contactt')

@app.route("/orderrlog")
def orderrlog():
	return render_template('orderrlog.html',title='orderrlog')

@app.route("/feedbacklog")
def feedbacklog():
	return render_template('feedbacklog.html',title='feedbacklog')

@app.route("/contacttlog")
def contacttlog():
	return render_template('contacttlog.html',title='contacttlog')


if __name__ == "__main__":
	app.run(debug=True)
