#!/usr/bin/env python3
from setuptools import find_packages, setup

setup(
    name='flask_boiler-api',
    version='0.1.0',
    description="Boilerplate Flask application",
    url='https://github.com/stewartmoreland/flack-boiler',
    include_package_data=True,
    install_requires=[
        'flask==1.1.1',
        'Flask-SQLAlchemy==2.4.4',
        'Flask-Alembic==2.0.1'
    ],
    setup_requires=[
        'pytest-runner'
    ],
    tests_require=[
        'pytest==4.5.0',
        'mock==3.0.5'
    ],
    entry_points={
        'console_scripts': [
            'flask_boiler-api = flask_boiler.main:main',
        ]
    }
)
