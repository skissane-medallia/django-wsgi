##############################################################################
#
# Copyright (c) 2010-2015, 2degrees Limited.
# All Rights Reserved.
#
# This file is part of django-wsgi <https://github.com/2degrees/django-wsgi/>,
# which is subject to the provisions of the BSD at
# <http://dev.2degreesnetwork.com/p/2degrees-license.html>. A copy of the
# license should accompany this distribution. THIS SOFTWARE IS PROVIDED "AS IS"
# AND ANY AND ALL EXPRESS OR IMPLIED WARRANTIES ARE DISCLAIMED, INCLUDING, BUT
# NOT LIMITED TO, THE IMPLIED WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST
# INFRINGEMENT, AND FITNESS FOR A PARTICULAR PURPOSE.
#
##############################################################################

import os

from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, "README.md")).read()
version = open(os.path.join(here, "VERSION.txt")).readline().rstrip()

setup(
    name="django-wsgi2",
    version=version,
    description="Enhanced WSGI support (for Django 3.x)",
    long_description=README,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI",
        "Topic :: Security",
    ],
    keywords="django wsgi webob web",
    author="Fernando Morales",
    author_email="fmoralesalcaide@protonmail.com",
    url="https://github.com/fmoralesalcaide/django-wsgi",
    license="BSD (http://dev.2degreesnetwork.com/p/2degrees-license.html)",
    packages=find_packages(exclude=["tests"]),
    zip_safe=False,
    tests_require=["coverage", "pynose"],
    install_requires=[
        "django >= 3.0, < 4",
        "WebOb >= 1.5",
        "six==1.16.0",
        "setuptools",
    ],
    test_suite="nose.collector",
)
