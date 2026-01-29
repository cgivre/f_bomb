#!/usr/bin/env python

# Copyright (c) 2014 SeatGeek

# This file is part of f_bomb.

from f_bomb import __version__
from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setup(
    name='f_bomb',
    version=__version__,
    author='Charles Givre',
    author_email='charles.givre@gtkcyber.com',
    packages=['f_bomb'],
    # keep for backwards compatibility of projects depending on `thefuzz[speedup]`
    install_requires=['rapidfuzz>=3.0.0, < 4.0.0'],
    url='https://github.com/seatgeek/thefuzz',
    license="MIT",
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Programming Language :: Python :: 3 :: Only',
    ],
    description='When you need an f-bomb in your code, look no further.',
    long_description=long_description,
    zip_safe=True,
    python_requires='>=3.8'
)
