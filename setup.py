#!/usr/bin/python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name = 'Daemonify',
    version = '0.1',
    author = 'Alex Prengère',
    author_email = 'alexprengere@gmail.com',
    url = 'https://github.com/alexprengere/daemonify',
    description = 'Daemonize a Python script.',
    long_description = open('README.rst').read(),
    py_modules = [
        'daemonify',
    ],
    data_files = [
        ('examples', [
            'examples/DaemonExample.py'
        ])
    ]
)
