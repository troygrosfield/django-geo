# -*- coding: utf-8 -*-
import os

from setuptools import find_packages
from setuptools import setup


classifiers = [
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Internet :: WWW/HTTP',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
]

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

setup(
    name='django-geo',
    version='0.0.1',
    description='Geo app for django',
    long_description=README,
    author='Troy Grosfield',
    maintainer='Troy Grosfield',
    url='https://github.com/infoagetech/django-geo',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    setup_requires=[
        'django >= 1.6',
    ],
    classifiers=classifiers
)
