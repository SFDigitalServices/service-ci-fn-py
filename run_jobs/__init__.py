""" status/http init file """
import os
import logging
import traceback
import urllib.request
import yaml
import azure.functions as func
from shared_code.common import func_json_response
from shared_code.common import func_jsend_response
from shared_code.common import validate_access
from mods.job_v1 import process as job_process

#pylint: disable=too-many-locals
def main(req: func.HttpRequest) -> func.HttpResponse:
    """ main function for run/step """
    logging.info('Run/Step processed a request.')

    try:
        validate_access(req)
        headers = {
            "Access-Control-Allow-Origin": "*"
        }

        if 'project' in req.params and 'job' in req.params:
            project_config_folder = os.getenv('PROJECT_CONFIG_FOLDER')
            project_config = f"{project_config_folder}/{req.params['project']}.yml"

            with urllib.request.urlopen(project_config) as file:
                config_yml = file.read().decode('utf-8')
                config_json = yaml.load(config_yml, Loader=yaml.SafeLoader)
                out = data = config_json

                if 'jobs' in data and req.params['job'] in data['jobs']:
                    out = job_process(data['jobs'][req.params['job']], \
                        req.get_json(), "run", req.params)

                return func_jsend_response(out, headers=headers, status_code=200)

        raise ValueError("Missing Project and/or Job")

    #pylint: disable=broad-except
    except Exception as err:
        logging.error("Run Step error occurred: %s", traceback.format_exc())
        return func_jsend_response(f"{err}", status_code=500)
