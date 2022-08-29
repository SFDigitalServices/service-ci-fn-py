""" airtable mod """
import os
from airtable import Airtable


def process(data: dict, content: dict, method: str, version: int):
    """ process content """
    if method == 'get' and version == 1:
        base = data['with']['AIRTABLE_BASE_KEY']
        table = data['with']['AIRTABLE_TABLE_NAME']
        key = os.environ.get('AIRTABLE_API_KEY')

        # init airtable
        airtable = get_airtable(base, table, key)

        row = airtable.get(content['airtable_record_id'])

        return row

    return content

def get_airtable(base, table, key):
    """ Get airtable """
    return Airtable(
        base,
        table,
        key)
