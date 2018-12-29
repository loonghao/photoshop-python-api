from setuptools import setup
import photoshop_python_api

setup(
    name='photoshop_python_api',
    version=photoshop_python_api.__version__,
    packages=['photoshop_python_api'],
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
    # description=SHORT,
    # long_description=LONG,
    test_suite='test',
    tests_require=['parameterized'],
    package_data={'': ['LICENSE']}
)
