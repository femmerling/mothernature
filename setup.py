#!/usr/bin/env python

from setuptools import setup

setup(
    name='MotherNature',
    version='0.1',
    description='Python Environment Manager',
    long_description="Manage python environment variables using yaml files.",
    author='Fauzan Emmerling',
    author_email='erich@emfeld.com',
    url='https://github.com/femmerling/mothernature',
    license='MIT',
    packages=['mothernature'],
    install_requires=['pyyaml'],
    zip_safe=False)
