""" formio v1 mod """
import os
from shared_code.formio import Formio

def process(data: dict, content: dict, method: str):
    """ process content """
    if method == 'submission-get':
        form_id = data['with']['FORMIO_FORM_ID']
        form_base = data['with']['FORMIO_BASE']
        submission = Formio.get_formio_submission_by_id(
            content['id'],
            form_id=form_id,
            base_url=os.environ.get(f"FORMIO_{form_base}_BASE_URL"),
            formio_api_key=os.environ.get(f"FORMIO_{form_base}_KEY"),
        )
        return submission

    return content
