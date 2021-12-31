import requests

password = "01x2253x6871"
config = requests.get("http://127.0.0.1:5000/api/get_config", {"password": password})
config = config.json()
print(config)
