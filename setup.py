#!/usr/bin/env python

from setuptools import setup, find_packages
import os, sys

# if you are not using vagrant, just delete os.link directly,
# The hard link only saves a little disk space, so you should not care
if os.environ.get('USER','') == 'vagrant':
    del os.link

setup(
    name='wilos-cli',
    version='0.1.0.0',
    description='Weather for Hackers.',
    author='Kevin Martin',
    license='MIT',
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stablegit
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
    keywords="live weather tool cli google darksky forecast",
    author_email='kvn.p.mrtn@gmail.com',
    url='https://github.com/aslan11/wilos-cli',
    packages=find_packages(),
    include_package_data = True,
    install_requires=[
        "click>=5.0",
        "requests==2.7.0"
    ] + (["colorama==0.3.3"] if "win" in sys.platform else []),
    entry_points={
        'console_scripts': [
            'wilos = wilos.main:main'
        ],
    }
)
