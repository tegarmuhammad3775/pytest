import requests

def test_get_list_of_users():
    url = "https://reqres.in/api/users?page=2"
    response = requests.get(url)
    respJson = response.json()
    assert response.status_code == 200
    assert respJson.get('page') == 2
