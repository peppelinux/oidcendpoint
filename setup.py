#!/usr/bin/env python
#
# Copyright (C) 2013 Umea Universitet, Sweden
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import re
import sys

from setuptools import setup
from setuptools.command.test import test as TestCommand

__author__ = 'Roland Hedberg'


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest

        errno = pytest.main(self.test_args)
        sys.exit(errno)


with open('src/oidcendpoint/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

setup(
    name="oidcendpoint",
    version=version,
    description="Python implementation of OAuth2 AS and OpenID Connect OP",
    author="Roland Hedberg",
    author_email="roland@catalogix.se",
    license="Apache 2.0",
    url='https://github.com/IdentityPython/oicsrv',
    packages=["oidcendpoint", 'oidcendpoint/oidc', 'oidcendpoint/authz',
              'oidcendpoint/user_authn', 'oidcendpoint/user_info',
              'oidcendpoint/oauth2', 'oidcendpoint/oidc/add_on',
              'oidcendpoint/common'],
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Libraries :: Python Modules"],
    extras_require={
        'docs': ['Sphinx', 'sphinx-autobuild', 'alabaster'],
        'quality': ['pylama', 'isort', 'eradicate', 'mypy', 'black', 'bandit'],
    },
    install_requires=[
        "oidcmsg>=0.6.8",
        "jinja2",
        "pyyaml",
        "requests",
        "responses"
        ],
    tests_require=[
        "pytest", "requests_mock", 'pytest-localserver'
        ],
    zip_safe=False,
    cmdclass={'test': PyTest},
    )
