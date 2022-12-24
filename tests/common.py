""" Test common and fixtures """
import os
import pytest

CLIENT_HEADERS = {
    "ACCESS_KEY": "1234567"
}

@pytest.fixture
def mock_env_access_key(monkeypatch):
    """ mock environment access key """
    monkeypatch.setenv("ACCESS_KEY", CLIENT_HEADERS["ACCESS_KEY"])
    monkeypatch.setenv("PROJECT_CONFIG_FOLDER",\
        "file://"+(os.path.join(os.path.dirname(__file__), "mocks")))
    monkeypatch.setenv("FORMIO_TEST_BASE_URL", "https://localhost/formio-test")
    monkeypatch.setenv("FORMIO_TEST_KEY", "test")
    monkeypatch.setenv("JSONATA_FN_JS_URL", "https://localhost/jsonata")
    monkeypatch.setenv("AIRTABLE_API_KEY", "test")
    monkeypatch.setenv("EMAIL_SVC_URL", "https://localhost/email")
    monkeypatch.setenv("EMAIL_SVC_KEY", "test")
    monkeypatch.setenv("PTS_TEST_URL", "https://localhost/pts-test")
    monkeypatch.setenv("PTS_TEST_KEY", "test")
    monkeypatch.setenv("BLUEBEAM_TEST_URL", "https://localhost/bluebeam-test")
    monkeypatch.setenv("BLUEBEAM_TEST_KEY", "test")

@pytest.fixture
def mock_env_no_access_key(monkeypatch):
    """ mock environment with no access key """
    monkeypatch.delenv("ACCESS_KEY", raising=False)
