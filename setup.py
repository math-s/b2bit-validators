#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

settings = dict()


# Publish Helper.
if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

settings.update(
    name='validators-b2bit',
    version='2021.9.24',
    description='General Validators',
    author='Matheus Andrade',
    author_email='matheus.andrade1996@gmail.com',
    url='https://github.com/math-s/API-3.0-Python',
    keywords='python sdk ecommerce validators',
    packages=find_packages(),
    install_requires=['requests', 'future'],
    license='MIT',
    classifiers=(
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    )
)


setup(**settings)

