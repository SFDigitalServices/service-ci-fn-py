""" status/http init file """
import os
import json
import logging
import threading
import traceback
import urllib.request
import requests
import jsend
import yaml
import azure.functions as func
from requests.models import Response
from shared_code.common import func_json_response
from shared_code.common import func_jsend_response
from shared_code.common import validate_access
from .step import Step

#pylint: disable=too-many-locals
def main(req: func.HttpRequest) -> func.HttpResponse:
    """ main function for run/step """
    logging.info('Run/Step processed a request.')

    try:
        validate_access(req)
        headers = {
            "Access-Control-Allow-Origin": "*"
        }

        if 'project' in req.params:
            project_config_folder = os.getenv('PROJECT_CONFIG_FOLDER')
            project_config = f"{project_config_folder}/{req.params['project']}.yml"

            with urllib.request.urlopen(project_config) as file:
                config_yml = file.read().decode('utf-8')
                config_json = yaml.load(config_yml, Loader=yaml.SafeLoader)
                out = data = config_json

                if 'job' in req.params and 'jobs' in data \
                    and req.params['job'] in data['jobs']:

                    out = data_job = data['jobs'][req.params['job']]

                    if 'step' in req.params and 'steps' in data_job:
                        step = int(req.params['step'])-1
                        step_last = len(data_job['steps'])-1
                        if 0 <= step <= step_last:

                            data_step = data_job['steps'][step]
                            out = Step.run(data_step, req.get_json())

                            if step + 1 <= step_last:
                                # trigger next step
                                print("next step")
                                data_step_next = data_job['steps'][step+1]
                                print(data_step_next)
                                if 'async' in data_step_next and data_step_next['async']:
                                    # running step async
                                    print("running async")
                                    thread = threading.Thread(
                                        target=Step.run,
                                        args=(data_step_next, out))
                                    thread.start()
                                else:
                                    out = Step.run(data_step_next, out)

                return func_jsend_response(out, headers=headers, status_code=200)

        raise ValueError("Missing Project")

    #pylint: disable=broad-except
    except Exception as err:
        logging.error("Run Step error occurred: %s", traceback.format_exc())
        msg_error = f"{err}"
        return func_jsend_response(msg_error, status_code=500)
