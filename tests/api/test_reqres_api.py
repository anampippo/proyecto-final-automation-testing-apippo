import pytest
import requests
from utils.logger import logger

BASE_URL = "https://reqres.in/api"

@pytest.mark.api
@pytest.mark.xfail(reason="ReqRes API bloquea requests automatizados (403)")
def test_get_users():
    logger.info("Probando GET /users?page=2")
    response = requests.get(f"{BASE_URL}/users?page=2")
    logger.info(f"Status code recibido: {response.status_code}")
    assert response.status_code == 200

@pytest.mark.api
@pytest.mark.xfail(reason="ReqRes API bloquea POST automatizado (403)")
def test_create_user():
    payload = {"name": "QA Tester", "job": "Automation"}
    logger.info(f"Probando POST /users con payload: {payload}")
    response = requests.post(f"{BASE_URL}/users", json=payload)
    logger.info(f"Status code recibido: {response.status_code}")
    assert response.status_code == 201

@pytest.mark.api
@pytest.mark.xfail(reason="ReqRes API bloquea DELETE automatizado (403)")
def test_delete_user():
    logger.info("Probando DELETE /users/2")
    response = requests.delete(f"{BASE_URL}/users/2")
    logger.info(f"Status code recibido: {response.status_code}")
    assert response.status_code == 204
