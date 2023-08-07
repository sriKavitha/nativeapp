
import requests

auth_token='R0g2vbUuaKSfjy6gFhS2AmLps0XhBPapvmXWTWuE5pROKAEPp8yXX2QH547r'
hed = {'Authorization': 'Bearer ' + auth_token}
data = {
    "password": "UQpb9y64FE",
    "username": "Qa5"
}

url = 'https://api-dev.mymov.com/api/v1/automation/users/delete'
response = requests.post(url, json=data, headers=hed)
print(response)
print(response.json())