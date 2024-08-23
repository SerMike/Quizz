import requests

# Define the parameters that we want to retrieve in the API call.
parameters = {
    "amount": 15,
    "type": "boolean",
    "category": 18
}

response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()

# Convert the JSON data into a python dictionary
data = response.json()

question_data = data["results"]
