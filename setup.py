from setuptools import setup, find_packages

def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name='KY040',
    version='1.0.0',
    description='A python module for reading the values from a KY040 rotary encoder module using a Raspberry Pi.',
    long_description=readme(),
    url='https://github.com/martinohanlon/KY040',
    author='Martin O\'Hanlon',
    license='MIT',
    packages=find_packages('.'),
    install_requires=[
      'RPi.GPIO',
    ],
    zip_safe=False
)
