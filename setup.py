#!/usr/bin/env python

from setuptools import setup

setup(
    name='MotherNature',
    version='0.2',
    description='Python Environment Variables Manager',
    long_description="Manage python environment variables easier using yaml files instead of cluttering your run comman.",
    author='Fauzan Emmerling',
    author_email='erich@emfeld.com',
    url='https://github.com/femmerling/mothernature',
    license='MIT',
    packages=['mothernature'],
    install_requires=['pyyaml'],
    zip_safe=False)
