#!/usr/bin/env python

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

readme = open('README.rst').read()
doclink = """
Documentation
-------------

The full documentation is at http://django-sqlalchemy.rtfd.org."""
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='django-sqlalchemy',
    version='0.0.1',
    description='Deploy static HTML sites to S3 with the simple 'alotofeffort' command.',
    long_description=readme + '\n\n' + doclink + '\n\n' + history,
    author='Asif Saifuddin Auvi',
    author_email='auvipy@gmail.com',
    url='https://github.com/trendbreaker/django-sqlalchemy',
    packages=[
        'django-sqlalchemy',
    ],
    package_dir={'django-sqlalchemy': 'django-sqlalchemy'},
    include_package_data=True,
    install_requires=[
    ],
    license='MIT',
    zip_safe=False,
    keywords='django-sqlalchemy',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
)
