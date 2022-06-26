import requests
import json
import pandas as pd
final_url = 'https://www.instagram.com/explore/tags/flipkart/?__a=1'
response = requests.get(final_url)
r = response.json()
# json_object = json.loads(r)
with open('data.json', 'w') as f:
    json.dump(r, f)

# pd.read_json("data.json").to_excel("data.xlsx")

pd.DataFrame(r).to_excel("output.xlsx")

