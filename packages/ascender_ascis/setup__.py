from setuptools import setup, find_packages
import os

calling_directory = os.path.dirname(os.path.abspath(__file__))
name_package = calling_directory.split("/")[-1]
_packages = find_packages(calling_directory)
print(_packages, calling_directory)

setup(
    name='ascis',
    version='0.1.0',
    packages=_packages,
    # include_package_data=True,
)