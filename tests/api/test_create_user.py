def test_create_user(api_session, base_url):
    payload = {
        "name": "John",
        "job": "developer"
    }
    response = api_session.post(f"{base_url}/users", json=payload)

    assert response.status_code == 201
    assert response.json()["name"] == "John"
    assert response.json()["job"] == "developer"