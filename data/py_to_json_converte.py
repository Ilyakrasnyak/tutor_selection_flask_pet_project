import json
from data import *


with open('goals.json', 'w') as g:
    g.write(json.dumps(goals))

with open('teachers.json', 'w') as g:
    g.write(json.dumps(teachers))
