import os
import re
from setuptools import setup, find_packages


def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search("^__version__ = ['\"]([^'\"]+)['\"]", init_py, re.MULTILINE).group(1)


setup(
    name='sixriver',
    setup_requires=[
        'marshmallow',
    ],
    install_requires=[
        'marshmallow',
    ],
    version=get_version('sixriver'),
    url='https://github.com/shiphero/sixriver',
    author='Sebastian Packmann',
    author_email='devsebas@gmail.com',
    description='A client for the 6River Api',
    license='MIT',
    package_dir={
        'sixriver': 'sixriver',
    },
    packages=find_packages(exclude=('tests', 'tests.*')),
    include_package_data=True,
    test_suite='tests',
    keywords="6river sixriver",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
