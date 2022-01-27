import requests

content = requests.get('https://studentportal.ipb.ac.id/Biodata/DataDiri')
print(content.status_code)

