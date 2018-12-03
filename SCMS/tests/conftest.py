import os
import pytest

from SCMS import create_app


@pytest.fixture
def app():
    app = create_app()

    yield app


@pytest.fixture
def client(app):
    """Test client for pytest"""

    return app.test_client()


def test_login(client):
    """Start with a blank database."""

    rv = client.post('/users/login',
                     data=dict(username='admin', password='admin12345'),
                     follow_redirects=True)
    print(rv.status)
    print(rv.location)
    print(rv.headers)
