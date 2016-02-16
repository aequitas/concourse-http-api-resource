#!/usr/bin/env python3

import logging as log
import os
import sys
import json
import tempfile
import requests

class HTTPResource:
    """HTTP resource implementation."""

    def cmd(self, arg, data):
        """Make the requests."""

        method = data.get('method', 'GET')
        uri = data['uri']
        headers = data['headers']
        json = data.get('json', None)

        response = requests.request(method, uri, json=json, headers=headers)

        log.info('http response code: %s', response.status_code)
        log.info('http response text: %s', response.text)

        return (response.status_code, response.text)

    def run(self, command_name: str, json_data: str, command_argument: str):
        """Parse input/arguments, perform requested command return output."""
        data = json.loads(json_data)

        # allow debug logging to console for tests
        if os.environ.get('RESOURCE_DEBUG', False) or data.get('source', {}).get('debug', False):
            log.basicConfig(level=log.DEBUG)
        else:
            logfile = tempfile.NamedTemporaryFile(delete=False)
            log.basicConfig(level=log.DEBUG, filename=logfile)

        log.debug('command: %s', command_name)
        log.debug('input: %s', data)
        log.debug('args: %s', command_argument)
        log.debug('environment: %s', os.environ)

        # initialize values with Concourse environment variables
        values = {k: v for k, v in os.environ.items() if k.startswith('BUILD_')}

        # combine source and params
        params = data.get('source', {})
        params.update(data.get('params', {}))

        # allow also to interpolate params
        values.update(params)

        # apply templating of environment variables onto parameters
        rendered_params = self._interpolate(params, values)

        output = self.cmd(command_argument, rendered_params)

        return json.dumps(output)

    def _interpolate(self, data, values):
        """Recursively apply values using format on all string key and values in data."""

        rendered = {}
        for k, v in data.items():
            if isinstance(k, str):
                k = k.format(**values)
            if isinstance(v, str):
                v = v.format(**values)
            elif isinstance(v, dict):
                v = self._interpolate(v, values)

            rendered[k] = v

        return rendered

print(HTTPResource().run(os.path.basename(__file__), sys.stdin.read(), sys.argv[1:]))
