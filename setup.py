# -*- coding: utf-8 -*-
""".

@file: setup.py
@guid: 9def386867704f9fbb8e7d4252fcaf60

@author: Yue Peng
@email: yuepaang@gmail.com
@date: 2019-07-30 09:08:42
@modified:

@brief:
"""
__author__ = "Yue Peng"

import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

#  requirements = [
#      'Jinja2==2.10',
#      'redis'
#  ]

setup_requirements = [

]

test_requirements = [
    'pytest'
]


setuptools.setup(
    name="panda-ypeng7",
    version="0.0.1",
    author="Yue Peng",
    author_email="yuepaang@gmail.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    entry_points={
    },
    #  install_requires=requirements,
    license="MIT license",
    url="https://github.com/ypeng7/panda",
    packages=setuptools.find_packages(include=["panda"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Natural Language :: English",
    ],
    include_package_data=True,
    keywords='panda',
    etup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    zip_safe=False
)
