""" bluebeam v1 mod """
import os
import json
import requests

def process(data: dict, content: dict, method: str, _params:dict):
    """ process content """
    if method == "project-create":
        env = data['with']['ENV']
        endpoint = os.environ.get(f"BLUEBEAM_{env}_URL")
        url = f"{endpoint}/submission"

        headers = {
            "ACCESS_KEY": os.environ.get(f"BLUEBEAM_{env}_KEY")
        }

        params = {}
        print(url)
        print(content)
        response = requests.post(url, headers=headers, data=json.dumps(content), \
            params=params, timeout=5)
        response_json = content
        print(response.status_code)
        print(response.content)
        if response.status_code == 200:
            try:
                response_json = json.loads(response.content)
            # pylint: disable=broad-except
            except Exception as err:
                print(f"jsonata.process Exception: {err}")
                response_json = {"data": str(response.content, 'utf-8')}

        return response_json
    return content