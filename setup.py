from setuptools import setup, find_packages
from titlecase import __version__

setup(
    name='python-titlecase',
    version=__version__,
    author='Stuart Colville, modified by Zach Snow',
    author_email='z@zachsnow.com',
    packages=find_packages(),
    url='https://github.com/zachsnow/python-titlecase/',
    license='LICENSE.rst',
    description=r"""Python port of John Gruber's titlecase""",
    long_description=open('README.rst').read(),
)
