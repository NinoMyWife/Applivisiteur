import requests
import json

BASE = "http://127.0.0.1:5000/"
VisitorName = "Tom"

response1 = requests.get(f"{BASE}getVisitors/{VisitorName}")
outputjson1 = response1.json()
print (f"{VisitorName} : " + json.dumps(outputjson1))
