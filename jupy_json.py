import json 

with open("bayesian_RL.ipynb", mode= "r", encoding= "utf-8") as f:
    myfile = json.loads(f.read())
myfile