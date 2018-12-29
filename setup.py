from setuptools import find_packages
from setuptools import setup

import photoshop_python_api

setup(
    name='photoshop_python_api',
    version=photoshop_python_api.__version__,
    package_dir={'': '.'},
    packages=find_packages('.'),
    url='https://github.com/loonghao/photoshop_python_api',
    author=photoshop_python_api.__author__,
    author_email='hoolongvfx@gmail.com',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=['pypiwin32==219'],
    package_data={'': ['LICENSE']},
    use_scm_version=True,
    setup_requires=['setuptools_scm']
)