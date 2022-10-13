""" email v1 mod """
import os
import json
import requests

def process(data: dict, content: dict, method: str):
    """ process content """
    if method == "send":
        endpoint = os.environ.get('EMAIL_SVC_URL')
        url = f"{endpoint}"

        headers = {
            "x-apikey": os.environ.get('EMAIL_SVC_KEY')
        }

        print(url)
        print(data)
        print(content)
        response = requests.post(url, headers=headers, data=json.dumps(content), timeout=5)
        response_json = content
        print(response.status_code)
        print(response.content)
        #pylint:disable=broad-except
        if response.status_code == 200:
            try:
                response_json = json.loads(response.content)
            except ValueError as err:
                print(f"email.process ValueError: {err}")
                response_json = {"data": str(response.content, 'utf-8')}
            except Exception as err:
                print(f"email.process Exception: {err}")
                response_json = {"data": str(response.content, 'utf-8')}

        return response_json
    return content
