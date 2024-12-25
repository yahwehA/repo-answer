# TODO решите задачу

import json

def task() -> float:
    with open('input.json', 'r') as file:
        data = json.load(file)
    total = 0

    for entry in data:
        score = entry.get("score", 0)
        weight = entry.get("weight", 0)
        total += score * weight
    return round(total, 3)

print(task())
