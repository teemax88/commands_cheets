import json

data = {
    "users": [
        {"Name": "Dominator", "skill": 100, "gold": 99999, "weapons": ['Sword', 'Atomic Laser'], "alive": True},
        {"Name": "Looser", "skill": 1, "gold": -100000, "weapons": [None, None, None], "alive": False},
    ]
}

with open("test_data.json", "w") as f:
    s = json.dumps(data, indent=4)
    f.write(s)
