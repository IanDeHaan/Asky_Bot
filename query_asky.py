import json
import requests
import random

def query(q):
    response = requests.get("https://api.asky.io/art")
    emotes = json.loads(response.text)
    valid = []
    for emote in emotes:
        if q.lower() in emote["title"].lower():
            valid.append(emote["content"])
    if len(valid) > 0:
        return (random.choice(valid)).lstrip()
    else:
        return "No emotes found (╥﹏╥)"