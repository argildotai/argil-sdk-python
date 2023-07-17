from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\\n" + fh.read()

setup(
    name='argil',
    version='0.0.29',#'{{VERSION_PLACEHOLDER}}',
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
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'requests',
    ],
    include_package_data=True,
    package_data={
        'argil': ['config.json'],
    },
    # package_dir = {"": "src"},
    # packages = setuptools.find_packages(where="src"),
    python_requires = ">=3.8"
)
