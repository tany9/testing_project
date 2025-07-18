import pytest

def test_delete_user(api_session, base_url):
    user_id = 2
    response = api_session.delete(f"{base_url}/users/{user_id}")
    
    assert response.status_code == 204