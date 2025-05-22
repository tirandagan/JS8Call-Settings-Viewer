#!/usr/bin/env python3

from setuptools import setup

setup(
    name="js8call-config-viewer",
    version="0.1.0",
    description="A terminal tool to view JS8Call.ini configuration files",
    author="backstop",
    py_modules=["js8call_config_viewer"],
    install_requires=["rich", "textual>=0.27.0"],
    entry_points={
        "console_scripts": [
            "js8call-config-viewer=js8call_config_viewer:main",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Ham Radio Enthusiasts",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Utilities",
    ],
) 