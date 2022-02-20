# QUE5 Write Python Script to get data using rest-api, Rest-Api Link :- http://api.open-notify.org/astros.json

print('Harry Goyal')
# code start
import requests                                       # include requests module which is used to send HTTP requests
base_url = 'http://api.open-notify.org/astros.json'   # web page link assign to variable
resp = requests.get(base_url)                         # sends a GET request to the specified url
data = resp.json()                                    # store output in json format
print(data)                                           # print the data
# code end