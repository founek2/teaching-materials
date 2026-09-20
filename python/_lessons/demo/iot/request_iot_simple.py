import requests

r = requests.post(
    "https://iotdomu.cz/api/device/61953025b24812001397e845/thing/led?property=power&value=true&api_key=n2z7NYrlDaGBQ832nNt9H4yWoBWZv5")
print(r)
