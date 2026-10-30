# testing /
import pytest
from app import app


@pytest.fixture()
def client():
    return app.test_client()
    

def test_nfl_page(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"NFL" in response.data


def test_nhl_page(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"NHL" in response.data


def test_nba_page(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"NBA" in response.data
