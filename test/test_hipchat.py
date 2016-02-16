import os

import pytest

from helpers import cmd

HIPCHAT_TOKEN = os.environ.get('HIPCHAT_TOKEN')

@pytest.mark.skipif(not HIPCHAT_TOKEN, reason='hipchat token not provided')
def test_hipchat_notify():
    """Test posting notification to Hipchat."""
    source = {
        'uri': 'https://www.hipchat.com/v2/room/2442416/notification',
        'headers': {
            'Authorization': 'Bearer ' + HIPCHAT_TOKEN
        },
        'method': 'POST',
    }

    params = {
        'json': {
            'color': 'green',
            'message': 'Build {BUILD_PIPELINE_NAME}/{BUILD_JOB_NAME}, nr: {BUILD_NAME} was a success!',
        }
    }

    response_code, text = cmd('out', source, params=params)

    assert response_code == 204
