import json
import pandas as pd
from pandas.io.json import json_normalize

#sample_json_df = pd.read_json('data/world_bank_projects.json')
#print(sample_json_df)


with open('data/world_bank_projects.json') as f:
    data = json.load(f)

for item in data:
    print(json.dumps(item, indent=4, sort_keys=True))
    exit(0)


df = json_normalize(data, 'countryshortname', ['project_name'])
print(x)