# QUE9 Write a script to upload a file sharepoint using python

print('Harry Goyal')
#code start
import requests
from shareplum import Office365
authcookie = Office365('https://trainingmy844.sharepoint.com', username='UserSharePoint@trainingmy844.onmicrosoft.com',password='SharePoint@123').GetCookies()
session = requests.Session()
session.cookies = authcookie
session.headers.update({'user-agent': 'python_bite/v1'})
session.headers.update({'accept': 'application/json;odata=verbose'})
session.headers.update({'X-RequestDigest': 'FormDigestValue'})
response = session.post(url="https://trainingmy844.sharepoint.com/sites/ForHackathon/_api/web/GetFolderByServerRelativeUrl('Harry Goyal')/Files/add(url='a.txt',overwrite=true)",data="")
session.headers.update({'X-RequestDigest': response.headers['X-RequestDigest']})
fileName = '/content/processes.html'
fileName = '/content/processes.csv'
with open(file_name, 'rb') as file_input:
    response = session.post(
        url="https://trainingmy844.sharepoint.com/sites/ForHackathon/_api/web/lists/getbytitle('ID-ROW-INTO-SHAREPOINT')/items(4)/AttachmentFiles/add(FileName='" + fileName + "')",data=file_input)
    print(response.text)
#code end