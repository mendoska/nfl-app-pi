#used to trim nfl week 10 json, makes it easier for testing.

import json 

with open("tests/fixtures/nfl_scoreboard_week10.json") as f:
    data = json.load(f)
    data["events"] = data["events"][:1]
with open("tests/fixtures/nfl_one_game.json", "w") as f:
    json.dump(data, f, indent=2)

