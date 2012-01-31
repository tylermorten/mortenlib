"""
Mortenlib
---------

All of my custom function used across my applications in python.

"""
from setuptools import setup

setup(
    name='Mortenlib',
    version='0.1.1',
    url='http://github.com/tylermorten/mortenlib',
    license='MIT',
    author='Tyler Morten',
    author_email='tyler@mpdigitalsolutions.com',
    description='My custom library of functions',
    long_description=__doc__,
    packages=['mortenlib'],
    platforms='any',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
