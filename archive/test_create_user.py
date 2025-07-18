import requests

def test_create_user():
    url = "https://reqres.in/api/users"
    payload = {
        "name": "Tanya",
        "job": "QA Engineer"
    }

    response = requests.post(url, json=payload)
    data = response.json()

    assert response.status_code == 201
    assert data["name"] == "Tanya"
    assert data["job"] == "QA Engineer"