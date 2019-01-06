from setuptools import find_packages
from setuptools import setup


setup(
    name='photoshop_python_api',
    package_dir={'': '.'},
    packages=find_packages('.'),
    url='https://github.com/loonghao/photoshop_python_api',
    author='Long Hao',
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
    install_requires=['comtypes'],
    package_data={'': ['LICENSE']},
    use_scm_version=True,
    setup_requires=['setuptools_scm']
)
