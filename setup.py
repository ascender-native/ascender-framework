from setuptools import setup

setup(
    name='ascender',
    version='0.1.0',
    py_modules=['ascender'],
    include_package_data=True,
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'ascender = ascender:cli',
        ],
    }
)