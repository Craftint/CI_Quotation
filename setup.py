# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in quotation_new/__init__.py
from quotation_new import __version__ as version

setup(
	name='quotation_new',
	version=version,
	description='quotation_new',
	author='frappe',
	author_email='info@craftinteractive.ae',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
