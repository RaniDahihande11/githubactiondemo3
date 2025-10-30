import requests
import pandas as pd
import os
#  to call api use --> requests

token = os.getenv("API_TOKEN") # for private api
print(f"Toekn: {token}")

if token=="1234abcd":
    print("Correct")
else:
    print('incorrect')


# response = requests.get('https://jsonplaceholder.typicode.com/users')
# data = response.json()
# df = pd.DataFrame(data)
# df = df [['id','name']] # want to show only id and name, this is called transformation
# print(df)
