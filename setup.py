#!/usr/bin/env python

from setuptools import setup

setup(
    name='django-form-utils',
    version='1.0.4',
    packages=['form_utils'],
    install_requires=[
        'django>=3.0',
    ],
    url='https://github.com/karlwnw/django-form-utils',
    license='BSD-3',
    author='Carl Meyer',
    author_email='carl@oddbird.net',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Libraries',
    ],
    description='Form utilities for Django'
)
