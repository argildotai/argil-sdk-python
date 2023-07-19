from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='argil',
    version='{{VERSION_PLACEHOLDER}}',
    author="Brivael Le Pogam",
    author_email="briva@argil.ai",
    description='SDK for the Argil API',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url='https://github.com/argildotai/argil-sdk-python',
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        "Programming Language :: Python :: 3",
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        "Programming Language :: Python :: 3 :: Only",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'requests',
    ],
    include_package_data=True,
    python_requires = ">=3.7"
)
