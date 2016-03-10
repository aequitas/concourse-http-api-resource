import json
import subprocess
from helpers import cmd
import pytest


def test_out(httpbin):
    """Test out action with minimal input."""

    data = {
        'source': {
            'uri': httpbin + '/status/200',
        }
    }
    subprocess.check_output('/opt/resource/out', input=json.dumps(data).encode())

def test_out_failure(httpbin):
    """Test action failing if not OK http response."""

    data = {
        'source': {
            'uri': httpbin + '/status/404',
        }
    }
    with pytest.raises(subprocess.CalledProcessError):
        subprocess.check_output('/opt/resource/out', input=json.dumps(data).encode())

def test_auth(httpbin):
    """Test basic authentication."""

    data = {
        'source': {
            'uri':  'http://user:password@{0.host}:{0.port}/basic-auth/user/password'.format(httpbin),
        }
    }
    subprocess.check_output('/opt/resource/out', input=json.dumps(data).encode())

def test_json(httpbin):
    """Json should be passed as JSON content."""

    source = {
        'uri': httpbin + '/post',
        'method': 'POST',
        'json': {
            'test': 123,
        },
    }

    output = cmd('out', source)

    assert output['json']['test'] == 123

def test_data_urlencode(httpbin):
    """Test passing URL encoded data."""

    source = {
        'uri': httpbin + '/post',
        'method': 'POST',
        'data_urlencode': {
            'field': {
                'test': 123,
            },
        },
    }

    output = cmd('out', source)

    assert output['form'] == {'field': '{"test": 123}'}
