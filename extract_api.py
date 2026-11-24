import requests
import pandas as pd
import os

os.makedirs("../data", exist_ok=True)

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)
response.raise_for_status()

df = pd.json_normalize(response.json())

output_file = "../data/users.csv"

df.to_csv(output_file, index=False)

print(f"Extracted {len(df)} records")
print(f"File created: {os.path.abspath(output_file)}")