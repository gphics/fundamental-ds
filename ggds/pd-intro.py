import pandas as pd
import json
score_data = {
    "vpt":[90,80,90],
    "vpc":[90,70,60],
    "vpm":[90,80,80],
    "vpr":[60,70,50],
}

df = pd.DataFrame(score_data)
df.to_json("ggds/score.json")


json.load()