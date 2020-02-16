"""Describe the distribution to distutils."""
from setuptools import find_packages
from setuptools import setup


setup(
    package_dir={'': 'src'},
    packages=find_packages('.'),
    setup_requires=["setuptools-scm", "setuptools>=40.0"],
    author_email='hal.long@outllok.com',
    install_requires=['comtypes==1.1.7'],
)
