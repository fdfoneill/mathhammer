#!/usr/bin/env/ python

import pathlib
from setuptools import setup

# the directory containing this file
HERE = pathlib.Path(__file__).parent

def readme():
	with open('README.md') as f:
		return f.read()

exec(open('mathhammer/_version.py').read())

setup(name='mathhammer',
	version=__version__,
	description='Analysis tool for Warhammer 40k',
	long_description=readme(),
	long_description_content_type='text/markdown',
	url='',
	author="F. Dan O'Neill",
	author_email="fdfoneill@gmail.com",
	license='MIT',
	packages=['mathhammer'],
	include_package_data=True,
	#third-party dependencies
	install_requires=[
		],
	#classifiers
	classifiers=[
		"License :: OSI Approved :: MIT License",
		"Programming Language :: Python :: 3",
		"Programming Language :: Python :: 3.7",
		],
	zip_safe=False,
	entry_points={}
	)