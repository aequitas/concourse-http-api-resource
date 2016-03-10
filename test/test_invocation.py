import json
import subprocess

import pytest


def test_out(httpserver):
    """Test out action with minimal input."""

    httpserver.serve_content(content='', code=200, headers=None)

    data = {
        'source': {
            'uri': httpserver.url,
        }
    }
    subprocess.check_output('/opt/resource/out', input=json.dumps(data).encode())

def test_out_failure(httpserver):
    """Test action failing if not OK http response."""

    httpserver.serve_content(content='', code=404, headers=None)

    data = {
        'source': {
            'uri': httpserver.url,
        }
    }
    with pytest.raises(subprocess.CalledProcessError):
        subprocess.check_output('/opt/resource/out', input=json.dumps(data).encode())
