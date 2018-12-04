from flask import Flask, render_template, request, redirect, url_for
from tinydb import TinyDB, Query
import os
import random

app = Flask("Shuffler")
port = int(os.environ.get("PORT", 5000))
team_names = []
db = TinyDB('names.json')

@app.route("/")
def index(team = None):
	return render_template("index.html", team = team)


@app.route("/shuffle")
def shuffle():
	if len(team_names):
		shuffled = sorted(team_names, key=lambda k: random.random())
		team = shuffled.pop()
		update_teams(shuffled)

		return render_template('index.html', team = team.upper())
	else:
		return render_template('index.html', done = True)


@app.route("/teams")
def teams():
	global team_names
	# Override the team names...
	# TODO: this can be done much better
	team_names=[]
	teams_from_db = db.all()
	for t in teams_from_db:
		team_names.append(t["name"])

	return render_template("teams.html", team_names=team_names)


@app.route("/user_input")
def user_input():
	new_name = request.args.get('team_name')
	db.insert({'name':new_name})

	return redirect(url_for('teams'))


@app.route("/delete")
def delete():
	global team_names
	db.purge()
	team_names=[]

	return redirect(url_for('teams'))

def update_teams(shuffled):
	global team_names
	team_names = shuffled

# Uncomment the line above if you want to run with the debug mode
# app.run(host='0.0.0.0', port=port, debug=True)
app.run(host='0.0.0.0', port=port)
