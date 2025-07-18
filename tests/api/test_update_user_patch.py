import requests

def test_update_user_patch(api_session, base_url):
    url = "https://reqres.in/api/users/2"
    payload = {
        "job": "QA Tester"
    }
    response = api_session.put(f"{base_url}/users/2", json=payload)

    assert response.status_code == 200
    assert response.json()["job"] == "QA Tester"