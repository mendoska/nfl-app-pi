import json
import responses
from app import fetch_espn_games

@responses.activate
def test_fetch_one_game():
    with open("tests/fixtures/nfl_one_game.json") as f:
        fake = json.load(f)
    responses.add(responses.GET, "https://fake-espn.test/scoreboard", json=fake)

    games = fetch_espn_games("https://fake-espn.test/scoreboard")

    assert len(games) == 1

    assert games[0]["home"] == "New York Giants"
    assert games[0]["away"] == "Washington Commanders"
    assert games[0]["home_score"] == 0
    assert games[0]["away_score"] == 0
    assert games[0]["home_logo"] == "https://a.espncdn.com/i/teamlogos/nfl/500/scoreboard/nyg.png"
    assert games[0]["away_logo"] == "https://a.espncdn.com/i/teamlogos/nfl/500/scoreboard/wsh.png"
    assert games[0]["status_text"] == "Thu, November 12th at 8:15 PM EST"
    assert games[0]["status_state"] == "UPCOMING"



    # #failed value to ensure it works 
    # assert games[0]["home"] == "Dallas Cowboys"

@responses.activate
def test_fetch_no_games():
    responses.add(responses.GET,"https://fake-espn.test/scoreboard",json={"events": []})

    games = fetch_espn_games("https://fake-espn.test/scoreboard")

    assert games ==[]         # what should come back when there are no games?

@responses.activate
def test_fetch_null_games():
    with open("tests/fixtures/nfl_null_game.json") as f:
        fake = json.load(f)
    responses.add(responses.GET,"https://fake-espn.test/scoreboard", json=fake)
    games = fetch_espn_games("https://fake-espn.test/scoreboard")

    assert games[0]["home_score"] == None 