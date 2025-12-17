import random 
import requests
from flask import Flask, render_template 

app = Flask (__name__)

def fetch_espn_games():
	url = "https://site.api.espn.com/apis/site/v2/sports/football/nfl/scoreboard"
	response = requests.get(url,timeout=10)
	data = response.json()

	#events is where the game data lives
	events = data.get("events" , [])
	games = []

	for event in events:
		#event game as a whole
		#competition the actual matchup 
		competition = event["competitions"][0]
		competitors = competition ["competitors"]
		#fetching status of the game
		status = competition["status"]["type"]["detail"]
		#state to show if game is live or not
		state = competition["status"]["type"]["state"] 

		#cleaning state verbage from espn API 
		if state == "in":
			status_state = "LIVE"
		elif state == "post":
			status_state = "FINAL"
		else:
			status_state = "UPCOMING"

		home_team = None
		away_team = None
		home_score = 0
		away_score = 0 

		#now that we have competitors
		for c in competitors:
			team_name = c["team"]["displayName"]
			score = int (c.get("score",0))

			if c["homeAway"] == "home":
				home_team = team_name
				home_score = score
			else:
				away_team = team_name
				away_score = score 
		games.append({
			"home": home_team,
			"away": away_team,
			"home_score": home_score,
			"away_score": away_score,
			"status_texts":status,
			"status_state": status_state
		})
	return games

@app.route("/")
def home():
	games = fetch_espn_games()
	#instead of returning text, now we look for HTML
	return render_template('index.html', games=games)

if __name__ == "__main__":
 	app.run(host = "0.0.0.0", port = 5000)
