import pytest
from flask import url_for
from dynamic_image_generator.main import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_index(client):
    response = client.get(url_for('index'))
    assert response.status_code == 200

def test_generate_certificate(client):
    response = client.post(url_for('generate_certificate'), data={'name': 'Test'})
    assert response.status_code == 200