""" PTS v1 mod """
import os
import json
import requests

def process(data: dict, content: dict, method: str, _params:dict):
    """ process content """
    if method == "permit-create":
        return pts_request_post(data['with']['ENV'], "/api/permit", content)
    return content

def pts_request_post(pts_env, path, content):
    """ pts request post """
    endpoint = os.environ.get(f"PTS_{pts_env}_URL")
    url = f"{endpoint}{path}"

    headers = {
        "x-api-key": os.environ.get(f"PTS_{pts_env}_KEY")
    }
    response = requests.post(url, headers=headers, data=json.dumps(content), timeout=5)
    response_json = content
    print(response.status_code)
    print(response.content)
    #pylint:disable=broad-except
    if response.status_code == 200:
        try:
            response_json = json.loads(response.content)
        except Exception as err:
            print(f"api.process Exception: {err}")
            response_json = {"data": str(response.content, 'utf-8')}
    return response_json
