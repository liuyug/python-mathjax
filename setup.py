#!/usr/bin/env python
# -*- encoding:utf-8 -*-

from setuptools import setup
from setuptools.command.install import install

from pymathjax import installSingleMathJax


class install_mathjax(install):
    def run(self):
        install.run(self)
        installSingleMathJax()


with open('README.md') as f:
    long_description = f.read()

setup(
    name='pymathjax',
    version='0.1.2',
    author='Yugang LIU',
    author_email='liuyug@gmail.com',
    url='https://github.com/liuyug/pymathjax.git',
    license='GPLv3',
    description='install MathJax on local',
    long_description=long_description,
    packages=['pymathjax'],
    cmdclass={
        'install': install_mathjax,
    }
)
