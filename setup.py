# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py
import os
from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='load-testing-app',
    version='0.1.0',
    description='Load Testing App',
    long_description=readme,
    author='Abhishek Surya',
    author_email='me@abhisheksurya.dev',
    url='https://github.com/abhisheksurya/load_testing_app',
    license=license,
    packages=find_packages(exclude=('test', 'doc')),
    install_requires=["pre-commit", "flake8", "black", "coverage", "sphinx", "nose", "pytest", "tox", "flit", "docopt", "pysqlite"]
)

