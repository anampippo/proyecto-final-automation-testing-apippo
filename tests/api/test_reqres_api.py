import pytest
import requests

BASE_URL = "https://reqres.in/api"

@pytest.mark.xfail(reason="ReqRes API bloquea requests automatizados (403)")
def test_get_users():
    response = requests.get(f"{BASE_URL}/users?page=2")
    assert response.status_code == 200

@pytest.mark.xfail(reason="ReqRes API bloquea POST automatizado (403)")
def test_create_user():
    payload = {"name": "QA Tester", "job": "Automation"}
    response = requests.post(f"{BASE_URL}/users", json=payload)
    assert response.status_code == 201

@pytest.mark.xfail(reason="ReqRes API bloquea DELETE automatizado (403)")
def test_delete_user():
    response = requests.delete(f"{BASE_URL}/users/2")
    assert response.status_code == 204
