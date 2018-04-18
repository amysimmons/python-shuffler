from flask import Flask, render_template
import random
import os

app = Flask("Shuffler")
port = int(os.environ.get("PORT", 5000))
teams = ['miami', 'dishroom', 'sf']

@app.route("/")
def index(team = None):
	return render_template("index.html", team = team)

@app.route("/shuffle")
def shuffle():
	if len(teams):
		shuffled = sorted(teams, key=lambda k: random.random())
		team = shuffled.pop()
		update_teams(shuffled)
		return render_template('index.html', team = team)
		#return redirect(url_for('index', team = team))
	else:
		return render_template('index.html', done = True)
		#return redirct(url_for('index', done = true))

def update_teams(shuffled):
	global teams
	teams = shuffled

app.run(host='0.0.0.0', port=port, debug=True).
