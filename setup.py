from setuptools import setup, find_packages

setup(
    name='argil-sdk',
    version='0.1.0',
    description='SDK for the Argil API',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
)
