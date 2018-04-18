from flask import Flask, render_template
import random

app = Flask("Shuffler")

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
		return render_template('index.html', team = team.upper())
		#return redirect(url_for('index', team = team))
	else:
		return render_template('index.html', done = True)
		#return redirct(url_for('index', done = true))

def update_teams(shuffled):
	global teams
	teams = shuffled

app.run(debug=True)
