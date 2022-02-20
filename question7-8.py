# QUE7 Write a Script to  Authenticate your github using Rest-API, Means Login

print('Harry Goyal')
# code start
import requests                                                      # include requests module which is used to send HTTP requests
access_token = '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'            # assign github personal access token
username = "harrygoyal123"                                           # github username
repository = "ansible"                                               # repository name
query_url = f"https://api.github.com/repos/{username}/{repository}"  # url
params = {
    "state": "open",
}
headers = {'Authorization': f'token {access_token}'}
result = requests.get(query_url, headers=headers, params=params)     # sends a GET request to the specified url with personal access token
print(result.json())                                                 # print output in json format
# code end