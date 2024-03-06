import requests

def test_create_new_user():
    url = "https://reqres.in/api/users"
    payload = {
        "name":"Paulo Oliviera",
        "job" : "producer"
    }
    response = requests.post(url, data=payload)
    respJson = response.json()
    assert response.status_code == 201
    assert respJson.get('name') == payload.get('name')