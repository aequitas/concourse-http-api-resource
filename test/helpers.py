import json
import os
import subprocess
import sys

ENVIRONMENT = {
    'BUILD_NAME': '1',
    'BUILD_JOB_NAME': 'test-job',
    'BUILD_PIPELINE_NAME': 'test-pipeline',
    'BUILD_ID': '123',
    'TEST': 'true',
}

def cmd(cmd_name, source, args: list = [], version={}, params={}):
    """Wrap command interaction for easier use with python objects."""

    in_json = json.dumps({
        "source": source,
        "version": version,
        "params": params,
    })
    command = ['/opt/resource/' + cmd_name] + args
    environment = dict(os.environ, **ENVIRONMENT)
    output = subprocess.check_output(command, env=environment,
        stderr=sys.stderr, input=bytes(in_json, 'utf-8'))

    return json.loads(output.decode())
