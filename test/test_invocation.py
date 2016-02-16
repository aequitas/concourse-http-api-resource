import json
import subprocess


def test_out():
    """Test out action with minimal input."""
    data = {
        'source': {
            'uri': 'http://example.com',
        }
    }
    subprocess.check_output('/opt/resource/out', input=json.dumps(data).encode())

def test_int():
    """Test if in returns empty object."""
    assert subprocess.check_output('/opt/resource/in', input='') == b'{}\n'
