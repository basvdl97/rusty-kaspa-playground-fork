"""
Kaspa Python SDK

A comprehensive Python SDK for interacting with the Kaspa blockchain network.
"""

from setuptools import setup, find_packages
import os

# Read the README file for long description
def read_long_description():
    here = os.path.abspath(os.path.dirname(__file__))
    readme_path = os.path.join(here, 'README.md')
    if os.path.exists(readme_path):
        with open(readme_path, encoding='utf-8') as f:
            return f.read()
    return ""

# Read version from package
def read_version():
    here = os.path.abspath(os.path.dirname(__file__))
    version_file = os.path.join(here, 'kaspa_sdk', '__version__.py')
    if os.path.exists(version_file):
        version_dict = {}
        with open(version_file) as f:
            exec(f.read(), version_dict)
        return version_dict['__version__']
    return "0.1.0"

setup(
    name='kaspa-sdk',
    version=read_version(),
    description='Python SDK for the Kaspa blockchain network',
    long_description=read_long_description(),
    long_description_content_type='text/markdown',
    author='Kaspa Developers',
    author_email='dev@kaspa.org',
    url='https://github.com/kaspanet/rusty-kaspa',
    project_urls={
        'Documentation': 'https://kaspa.aspectron.org/',
        'Source': 'https://github.com/kaspanet/rusty-kaspa',
        'Tracker': 'https://github.com/kaspanet/rusty-kaspa/issues',
    },
    license='ISC',
    packages=find_packages(exclude=['tests', 'tests.*', 'examples', 'examples.*', 'docs', 'docs.*']),
    python_requires='>=3.8',
    install_requires=[
        'websockets>=11.0',
        'cryptography>=41.0.0',
        'mnemonic>=0.20',
        'base58>=2.1.0',
        'pycryptodome>=3.18.0',
        'typing-extensions>=4.5.0; python_version < "3.10"',
    ],
    extras_require={
        'dev': [
            'pytest>=7.4.0',
            'pytest-asyncio>=0.21.0',
            'pytest-cov>=4.1.0',
            'black>=23.7.0',
            'flake8>=6.1.0',
            'mypy>=1.5.0',
            'isort>=5.12.0',
            'sphinx>=7.1.0',
            'sphinx-rtd-theme>=1.3.0',
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Security :: Cryptography',
        'Topic :: System :: Distributed Computing',
    ],
    keywords='kaspa blockchain cryptocurrency sdk wallet rpc',
    zip_safe=False,
    include_package_data=True,
)
