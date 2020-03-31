"""Describe the distribution to distutils."""
from setuptools import find_packages
from setuptools import setup


with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='photoshop_python_api',
    author='Long Hao',
    package_dir={'': 'src'},
    url='https://github.com/loonghao/photoshop_python_api',
    version='0.7.2',
    packages=find_packages('./src'),
    setup_requires=['setuptools-scm', 'setuptools>=40.0'],
    author_email='hal.long@outllok.com',
    install_requires=['comtypes==1.1.7'],
    description=(
        'The API for using COM (Component Object Model) objects '
        'interfaces of Photoshop.'
    ),
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: Microsoft :: Windows :: Windows 10',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
