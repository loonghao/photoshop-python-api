"""Describe the distribution to distutils."""
import re

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("src/photoshop/__init__.py", "r") as file_object:
    context = file_object.read()
    version = re.search(r'__version__\s*=\s*"([\d/.]+)"', context).groups()[0]

setup(
    name="photoshop_python_api",
    author="Long Hao",
    package_dir={"": "src"},
    url="https://github.com/loonghao/photoshop_python_api",
    version=version,
    packages=find_packages("./src"),
    setup_requires=["setuptools>=40.0"],
    author_email="hal.long@outlook.com",
    install_requires=["comtypes==1.1.7"],
    description="Python API for Photoshop.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: Microsoft :: Windows :: Windows 10",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
