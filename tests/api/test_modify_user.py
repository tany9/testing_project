import pytest

def test_create_user(api_session, base_url):
    payload = {
        "name": "John",
        "job": "QA Engineer"
    }
    response = api_session.post(f"{base_url}/users", json=payload)
    data = response.json()

    assert response.status_code == 201
    assert data["name"] == "John"
    assert data["job"] == "QA Engineer"
    assert "id" in data


def test_update_user_put(api_session, base_url):
    payload = {
        "name": "Anna",
        "job": "Senior QA"
    }
    response = api_session.put(f"{base_url}/users/2", json=payload)
    data = response.json()

    assert response.status_code == 200
    assert data["name"] == "Anna"
    assert data["job"] == "Senior QA"


def test_update_user_patch(api_session, base_url):
    payload = {
        "job": "Lead QA"
    }
    response = api_session.patch(f"{base_url}/users/2", json=payload)
    data = response.json()

    assert response.status_code == 200
    assert data["job"] == "Lead QA"