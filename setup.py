# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in erpnext_shopify_enhancer/__init__.py
from erpnext_shopify_enhancer import __version__ as version

setup(
	name='erpnext_shopify_enhancer',
	version=version,
	description='Customize shopify data to suite erpnext. ex. truncate item_name to 140 char',
	author='GreyCube Technologies',
	author_email='admin@greycube.in',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
