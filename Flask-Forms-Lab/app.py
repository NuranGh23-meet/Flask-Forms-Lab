from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


username = "Nuran"
password = "12345"
facebook_friends=["lynne","mayar","nour", "nardin", "masa", "natal", "nurcin"]


@app.route('/', methods=['GET', 'POST'])  # '/' for the default page
def login():
	if request.method == 'GET':
		return render_template('login.html')
	else: 
		if username == request.form['username'] and password == request.form['password']:
			return redirect(url_for('home'))			
		else: 
			return redirect(url_for('login'))


@app.route("/home")
def home():
	return render_template('home.html', facebook_friends=facebook_friends)

@app.route('/friend_exists/<string:friend>', methods = ['GET' , 'POST'])
def friend(friend):
	# for f in facebook_friends:
	# 	f = f.lower()
	# friend = friend.lower()
	is_friend = False
	if friend in facebook_friends:
		is_friend = True

	return render_template("friend_exists.html", friends_exists = is_friend)


if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)