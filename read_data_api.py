import requests
import pandas as pd

#  to call api use --> requests

response = requests.get('https://jsonplaceholder.typicode.com/users')
data = response.json()
df = pd.DataFrame(data)

print(df)
