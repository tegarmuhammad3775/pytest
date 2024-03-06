import requests

def test_create_new_user():
    url = "https://fakerestapi.azurewebsites.net/api/v1/Users"
    payload = {
        "id":10,
        "userName":"PauloOliviera",
        "password" : "12345"
    }
    headers = {'Content-Type': 'application/json'}
    
    response = requests.get(url, data=payload)
    respJson = response.json()
    assert response.status_code == 200
