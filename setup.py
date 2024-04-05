from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

packages = find_packages()

setup(
    name='ascender',
    version='0.1.0',
    packages=packages, 
    py_modules=['ascender'],
    include_package_data=True,
    install_requires=requirements + [
        'click',
    ],
    entry_points={
        'console_scripts': [
            'ascender=ascender:cli',
        ],
    },
)