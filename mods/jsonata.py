""" jsonata mod """
import os
import json
import requests

def process(data: dict, content: dict, method: str, version: int):
    """ process content """
    if method == "eval" and version == 1:
        endpoint = os.environ.get('JSONATA_FN_JS_URL')
        jsonata = data['with']['JSONATA_MAPPING']
        url = f"{endpoint}/api/eval"

        headers = {}

        params = {
            "jsonata": jsonata
        }
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
            #pylint: disable=broad-except
            except Exception as err:
                print(f"jsonata.process Eception: {err}")
                response_json = {"data": str(response.content, 'utf-8')}

        return response_json
    return content
