""" Test for run/jobs endpoint """
# pylint: disable=redefined-outer-name,unused-argument,unused-import
import os
import json
from unittest.mock import patch
import azure.functions as func
from tests.common import mock_env_access_key, mock_env_no_access_key, CLIENT_HEADERS
from run_jobs import main

def test_run_jobs_function(mock_env_access_key):
    """ test run_jobs function """
    # Construct a mock HTTP request.
    params = {"project": "test_proj_config",\
        "job": "job1"}
    body = bytes('{"test": "hello"}', encoding="UTF-8")

    req = func.HttpRequest(
        method='GET',
        headers=CLIENT_HEADERS,
        params=params,
        body=body,
        url='/api/run/jobs')

    with patch('mods.email_v1.requests.post') as mock:
        mock.return_value.status_code.return_value\
            = 200
        # Call the function.
        resp = main(req)
        # print response body
        print(resp.get_body())
        # loads response body as json
        resp_json = json.loads(resp.get_body())

        # Check the output.
        assert resp_json['status'] == 'success'

def test_run_jobs_function_error(mock_env_access_key):
    """ test run_jobs function """
    # Construct a mock HTTP request.
    req = func.HttpRequest(
        method='GET',
        headers=CLIENT_HEADERS,
        body=None,
        url='/api/run/jobs')

    # Call the function.
    resp = main(req)
    # print response body
    print(resp.get_body())
    # loads response body as json
    resp_json = json.loads(resp.get_body())

    # Check the output.
    assert resp_json['status'] == 'error'


def test_run_jobs_functio_access_error(mock_env_no_access_key):
    """ test run_jobs function """
    # Construct a mock HTTP request.
    params = {"project": "mock_prj", "job": "mock_job"}
    req = func.HttpRequest(
        method='GET',
        params=params,
        body=None,
        url='/api/run/jobs')

    # Call the function.
    resp = main(req)
    # print response body
    print(resp.get_body())
    # loads response body as json
    resp_json = json.loads(resp.get_body())

    # Check the output.
    assert resp_json['status'] == 'error'
    assert "Access Denied" in resp_json['message']
