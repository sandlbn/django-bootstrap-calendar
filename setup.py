#!/usr/bin/env python

import os
import sys

import django_bootstrap_calendar

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = django_bootstrap_calendar.__version__

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='django-bootstrap-calendar',
    version=version,
    description='simple calendar based on the calendar of http://bootstrap-calendar.azurewebsites.net/',
    long_description=readme + '\n\n' + history,
    author='Marcin Spoczynski',
    author_email='marcin@spoczynski.com',
    url='https://github.com/sandlbn/django_bootstrap_calendar',
    packages=[
        'django_bootstrap_calendar',
    ],
    include_package_data=True,
    install_requires=[
        'jsmin',
    ],
    license="BSD",
    zip_safe=False,
    keywords='django_bootstrap_calendar',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
)
