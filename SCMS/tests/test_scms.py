import os
import pytest


def test_login(app):
    resp = client.get(url_for('admin.login')).status_code
    print(resp)
