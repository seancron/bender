from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name='bender',

    version='0.1.0',

    description="Python chat bot framework",
    url='https://github.com/seancron/bender',

    author='Sean Cronin',
    author_email='seancron@gmail.com',

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
    ],

    keywords='slack chat api',

    packages=['bender', 'bender.plugins'],
    install_requires=['slack-rtm', 'blinker>=1.3'],
    dependency_links=[
        'git+https://github.com/seancron/slack-rtm.git'
    ]
)
