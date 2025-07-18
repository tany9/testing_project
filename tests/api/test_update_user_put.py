import requests

def test_update_user_put(api_session, base_url):
    payload = {
        "name": "Anna",
        "job": "Automation Engineer"
    }
    response = api_session.put(f"{base_url}/users/2", json=payload)

    assert response.status_code == 200
    assert response.json()["name"] == "Anna"
    assert response.json()["job"] == "Automation Engineer"