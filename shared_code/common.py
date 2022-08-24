""" Common shared functions """
import os
import json
import jsend
import azure.functions as func

def func_json_response(response, headers=None, json_root="items"):
    """ json func_json_response """
    json_data = json.loads(response.text)
    func_status_code = response.status_code

    if response.status_code == 200:
        func_response = {json_root: json_data}
    else:
        func_response = json.dumps(json_data)

    return func_jsend_response(
            func_response, headers=headers, status_code=func_status_code)

def func_jsend_response(body, headers=None, status_code=200):
    """ func_jsend_success_response """
    if 200 <= status_code < 300:
        func_response = json.dumps(jsend.success(body))
    elif 400 <= status_code < 500:
        func_response = json.dumps(jsend.fail(body))
    else:
        func_response = json.dumps(jsend.error(body))

    return func.HttpResponse(
        func_response,
        status_code=status_code,
        mimetype="application/json",
        headers=headers
    )

def validate_access(req: func.HttpRequest):
    """ validate access method """
    access_key = os.getenv('ACCESS_KEY')
    if not access_key or req.headers.get('ACCESS_KEY') != access_key:
        raise ValueError("Access Denied")
