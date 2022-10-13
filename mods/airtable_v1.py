""" airtable v1 mod """
import os
from airtable import Airtable


def process(data: dict, content: dict, method: str):
    """ process content """

    base = data['with']['AIRTABLE_BASE_KEY']
    table = data['with']['AIRTABLE_TABLE_NAME']
    key = os.environ.get('AIRTABLE_API_KEY')

    # init airtable
    airtable = get_airtable(base, table, key)

    if method == 'get' :
        row = airtable.get(content['airtable_record_id'])
        return row
    if method == 'insert' :
        airtable_record = airtable.insert(content)
        return airtable_record

    return content

def get_airtable(base, table, key):
    """ Get airtable """
    return Airtable(
        base,
        table,
        key)
