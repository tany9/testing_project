import pytest

@pytest.mark.parametrize("user_id", [1, 2, 3])
def test_get_user_by_id(api_session, user_id):
    url = f"https://reqres.in/api/users/{user_id}"
    response = api_session.get(url)
    data = response.json()

    assert response.status_code == 200
    assert data["data"]["id"] == user_id
    assert "email" in data["data"]