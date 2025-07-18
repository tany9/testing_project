import json
import requests
import pytest

def load_test_data():
    with open("data/user_data.json", encoding="utf-8") as file:
        return json.load(file)

@pytest.mark.parametrize("user_data", load_test_data())
def test_create_user_from_json(user_data):
    url = "https://reqres.in/api/users"
    response = requests.post(url, json=user_data)
    data = response.json()

    assert response.status_code == 201
    assert data["name"] == user_data["name"]
    assert data["job"] == user_data["job"]