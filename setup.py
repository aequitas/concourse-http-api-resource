#!/usr/bin/env python3

import os

from setuptools import find_packages, setup

setup(
    name='http-api-resource',
    packages=find_packages('assets'),

    version='0.0.0',

    install_requires=['webcolors', 'docopt', 'requests', 'rcfile', 'jenkinsapi', 'retry'],
    entry_points={
        'console_scripts': [
            'out = resource:main',
        ],
    },
)
